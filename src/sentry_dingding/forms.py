# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token'
    )
    fix_project_name = forms.CharField(
        max_length=20,
        help_text=u'在这可以自定义修正中文项目名字，钉钉上送错误信息将提示错误来自此项目明',
        required = False
    )
    ignore_regular = forms.CharField(
        max_length=1255,
        help_text=u'忽略该消息字符串，如果报错信息中含有该字符串，将不会推送到钉钉，多个匹配字符串使用 || 分割。',
        required = False
    )
    highest_level_regular = forms.CharField(
        max_length=1255,
        help_text=u'高危信息报错，如果报错信息中含有该字符串，钉钉将会推送高危信息消息，多个匹配字符串使用||分割。例子： A接口异常||B登录失败||TIFA is not defined',
        required = False
    )
    medium_level_regular = forms.CharField(
        max_length=1255,
        help_text=u'中级危险信息报错，如果报错信息中含有该字符串，钉钉将会推送中危信息消息，多个匹配字符串使用 || 分割。',
        required = False
    )
    low_level_regular = forms.CharField(
        max_length=1255,
        help_text=u'低级危险信息报错，如果报错信息中含有该字符串，钉钉将会推送低危信息消息，多个匹配字符串使用 || 分割。',
        required = False
    )