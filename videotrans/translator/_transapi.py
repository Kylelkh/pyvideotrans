# -*- coding: utf-8 -*-
import os
import re
import time
from urllib.parse import quote

import requests

from videotrans.configure import config
from videotrans.translator._base import BaseTrans
from videotrans.util import tools


class TransAPI(BaseTrans):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        url = config.params['trans_api_url'].strip().rstrip('/').lower()
        if not url.startswith('http'):
            url = f"http://{url}"
        self.api_url=url+ ('&' if url.find('?') > 0 else '/?')
        pro = self._set_proxy(type='set')
        if pro:
            self.proxies = {"https": pro, "http": pro}


    # 实际发出请求获取结果
    def _get_content(self,data:list):
        text=quote("\n".join(data))
        requrl = f"{self.api_url}target_language={self.target_language}&source_language={self.source_code}&text={text}&secret={config.params['trans_secret']}"
        config.logger.info(f'[TransAPI]请求数据：{requrl=}')
        response = requests.get(url=requrl, proxies=self.proxies)
        config.logger.info(f'[TransAPI]返回:{response.text=}')
        if response.status_code != 200:
            raise Exception(f'code={response.status_code=},{response.text}')
        jsdata = response.json()
        if jsdata['code'] != 0:
            raise Exception(jsdata['msg'])
        return jsdata['text']

def trans(text_list, target_language="en", *, set_p=True, inst=None, stop=0, source_code="", is_test=False, uuid=None):
    """
    text_list:
        可能是多行字符串，也可能是格式化后的字幕对象数组
    target_language:
        目标语言
    set_p:
        是否实时输出日志，主界面中需要
    """
    wait_sec = 0.5
    try:
        wait_sec = int(config.settings['translation_wait'])
    except Exception:
        pass
    # 翻译后的文本

    url = config.params['trans_api_url'].strip().rstrip('/').lower()
    if len(config.params['trans_api_url'].strip()) < 10:
        raise Exception(
            'TRANS API 接口不正确，请到设置中重新填写' if config.defaulelang == 'zh' else 'TRANS API interface is not correct, please go to Settings to fill in again')

    if not url.startswith('http'):
        url = f"http://{url}"
    if url.find('?') > 0:
        url += '&'
    else:
        url += '/?'


    def get_content(data):

        requrl = f"{url}target_language={data['target_language']}&source_language={data['source_language']}&text={data['text']}&secret={data['secret']}"
        config.logger.info(f'[TransAPI]请求数据：{requrl=}')
        response = requests.get(url=requrl, proxies=proxies)
        config.logger.info(f'[TransAPI]返回:{response.text=}')
        if response.status_code != 200:
            raise Exception(f'code={response.status_code=},{response.text}')
        jsdata = response.json()
        if jsdata['code'] != 0:
            raise Exception(jsdata['msg'])
        return jsdata['text']

    target_text = []
    index = -1  # 当前循环需要开始的 i 数字,小于index的则跳过
    iter_num = 0  # 当前循环次数，如果 大于 config.settings.retries 出错
    err = ""
    while 1:
        if config.exit_soft or (config.current_status != 'ing' and config.box_trans != 'ing' and not is_test):
            return

        if iter_num > int(config.settings['retries']):
            err = f'{iter_num}{"次重试后依然出错" if config.defaulelang == "zh" else " retries after error persists "}:{err}'
            break
        if iter_num >= 1:
            if set_p:
                tools.set_process(
                    f"第{iter_num}次出错重试" if config.defaulelang == 'zh' else f'{iter_num} retries after error',
                    type="logs",
                    uuid=uuid)
            time.sleep(5)
        iter_num += 1
        # 整理待翻译的文字为 List[str]
        if isinstance(text_list, str):
            source_text = text_list.strip().split("\n")
        else:
            source_text = [t['text'] for t in text_list]

        # 切割为每次翻译多少行，值在 set.ini 中设定，默认10
        split_size = int(config.settings['trans_thread'])
        split_source_text = [source_text[i:i + split_size] for i in range(0, len(source_text), split_size)]
        response = None
        for i, it in enumerate(split_source_text):
            if config.exit_soft or (config.current_status != 'ing' and config.box_trans != 'ing' and not is_test):
                return
            if i <= index:
                continue
            if stop > 0:
                time.sleep(stop)
            try:
                data = {
                    "text": quote("\n".join(it)),
                    "secret": config.params['trans_secret'],
                    "source_language": '',
                    "target_language": 'zh' if target_language.startswith('zh') else target_language
                }

                result = get_content(data)
                result = tools.cleartext(result).split("\n")
                if not result:
                    err = f'no translation result'
                    break
                source_length = len(it)
                result_length = len(result)
                # 如果返回数量和原始语言数量不一致，则重新切割
                if result_length < source_length:
                    config.logger.info(f'翻译前后数量不一致，需要重新按行翻译')
                    result = []
                    for line_res in it:
                        data['text'] = line_res
                        time.sleep(wait_sec)
                        result.append(get_content(data))

                if inst and inst.precent < 75:
                    inst.precent += round((i + 1) * 5 / len(split_source_text), 2)
                if set_p:
                    tools.set_process(
                        f'{result[0]}\n\n' if split_size == 1 else "\n\n".join(result),
                        type='subtitle',
                        uuid=uuid)
                    tools.set_process(
                        config.transobj['starttrans'] + f' {i * split_size + 1} ',
                        type="logs",
                        uuid=uuid)
                result_length = len(result)
                while result_length < source_length:
                    result.append("")
                    result_length += 1
                result = result[:source_length]
                target_text.extend(result)
            except requests.ConnectionError as e:
                err = str(e)
                break
            except Exception as e:
                err = str(e)
                time.sleep(wait_sec)
                config.logger.error(f'翻译出错:暂停{wait_sec}s')
                break
            else:
                # 未出错
                err = ''
                iter_num = 0
                index = i
        else:
            break
    if shound_del:
        update_proxy(type='del')
    if err:
        config.logger.error(f'[TransAPI]翻译请求失败:{err=}')
        raise Exception(f'Trans_API:{err}')
    if isinstance(text_list, str):
        return "\n".join(target_text)

    max_i = len(target_text)
    if max_i < len(text_list) / 2:
        raise Exception(f'Trans_API:{config.transobj["fanyicuowu2"]}')
    for i, it in enumerate(text_list):
        if i < max_i:
            text_list[i]['text'] = target_text[i]
        else:
            text_list[i]['text'] = ""
    return text_list