# coding: utf-8

import json
import logging

import requests
from sentry.plugins.bases.notify import NotificationPlugin

import sentry_dingding
from .forms import DingDingOptionsForm

DingTalk_API = "https://oapi.dingtalk.com/robot/send?access_token={token}"


class DingDingPlugin(NotificationPlugin):
    """
    Sentry plugin to send error counts to DingDing.
    """
    author = 'ansheng'
    author_url = 'https://github.com/anshengme/sentry-dingding'
    version = sentry_dingding.VERSION
    description = 'Send error counts to DingDing.'
    resource_links = [
        ('Source', 'https://github.com/anshengme/sentry-dingding'),
        ('Bug Tracker', 'https://github.com/anshengme/sentry-dingding/issues'),
        ('README', 'https://github.com/anshengme/sentry-dingding/blob/master/README.md'),
    ]

    slug = 'DingDing'
    title = 'DingDing'
    conf_key = slug
    conf_title = title
    project_conf_form = DingDingOptionsForm

    def is_configured(self, project):
        """
        Check if plugin is configured.
        """
        return bool(self.get_option('access_token', project))

    def notify_users(self, group, event, *args, **kwargs):
        self.post_process(group, event, *args, **kwargs)

    def post_process(self, group, event, *args, **kwargs):
        """
        Process error.
        """
        if not self.is_configured(group.project):
            return

        if group.is_ignored():
            return

        access_token = self.get_option('access_token', group.project)

        # ignore_regular = self.get_option('ignore_regular', group.project)
        # highest_level_regular = self.get_option('highest_level_regular', group.project)
        # medium_level_regular = self.get_option('medium_level_regular', group.project)
        # low_level_regular = self.get_option('low_level_regular', group.project)
        

        send_url = DingTalk_API.format(token=access_token)

        resultDingStrObj = self.getDingTitles(group, event, *args, **kwargs)

        # 忽略的消息不上送钉钉
        if (not resultDingStrObj):
            return


        #title = u"**【高危】错误信息预警**来自 {}".format(event.project.slug)

        # data = {
        #     "msgtype": "markdown",
        #     "markdown": {
        #         "title": resultDingStrObj["firstScreenTitle"],
        #         "text": u"#### {title} \n > {message} [href]({url})".format(
        #             title=resultDingStrObj["contentTitle"],
        #             message=event.message,
        #             url=u"{}events/{}/".format(group.get_absolute_url(), event.id),
        #         )
        #     },
        #     "at": {
        #         "isAtAll": True
        #     }
        # }
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": 'dsads',
                "text": '### markdowm 艾特全体测试 \n 打撒的撒'
            },
            "at": {
                "isAtAll": True
            }
        }
        requests.post(
            url=send_url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )
    def getDingTitles(self, group, event, *args, **kwargs):

        ignore_regular = self.get_option('ignore_regular', group.project)
        highest_level_regular = self.get_option('highest_level_regular', group.project)
        medium_level_regular = self.get_option('medium_level_regular', group.project)
        low_level_regular = self.get_option('low_level_regular', group.project)
        fix_project_name = self.get_option('fix_project_name', group.project)
        fix_project_name = fix_project_name if bool(fix_project_name) else event.project.slug

        resultDingStrObj = {}
        resultDingStrObj["firstScreenTitle"] = u"New error from {}".format(fix_project_name)
        resultDingStrObj["contentTitle"] = u"New error from {}".format(fix_project_name)
        resultDingStrObj["isNeedAtAll"] = False

        # 错误信息分级判断
        isIgnoreMessage = self.regularInMessage(ignore_regular, event.message)
        isHighLevel = self.regularInMessage(highest_level_regular, event.message)
        isMediumLevel = self.regularInMessage(medium_level_regular, event.message)
        isLowLevel = self.regularInMessage(low_level_regular, event.message)

        # 处理高危错误
        if isHighLevel:      
            resultDingStrObj["firstScreenTitle"] = u"【高危错误!!请及时处理】来自 {}".format(fix_project_name)
            resultDingStrObj["contentTitle"] = u"**【高危】错误信息**来自 {}".format(fix_project_name)
            resultDingStrObj["isNeedAtAll"] = True
            return resultDingStrObj

        # 处理中危错误
        if isMediumLevel:
            resultDingStrObj["firstScreenTitle"] = u"【中危错误!】来自 {}".format(fix_project_name)
            resultDingStrObj["contentTitle"] = u"**【中危】错误信息**来自 {}".format(fix_project_name)
            return resultDingStrObj

        # 处理低级危错误
        if isLowLevel:
            resultDingStrObj["firstScreenTitle"] = u"【低危错误】来自 {}".format(fix_project_name)
            resultDingStrObj["contentTitle"] = u"【低危】错误信息来自 {}".format(fix_project_name)
            return resultDingStrObj

        # 处理忽略错误
        if isIgnoreMessage:
            return False  

        return resultDingStrObj

    def regularInMessage (self, inputSrt, message):
        if (bool(inputSrt)):
            strArr = inputSrt.split("||") 
            for item in strArr:
                if item in message:
                    return True
        else:
            return False    






