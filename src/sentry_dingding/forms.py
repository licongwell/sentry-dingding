# coding: utf-8

from django import forms


class DingDingOptionsForm(forms.Form):
    access_token = forms.CharField(
        max_length=255,
        help_text='DingTalk robot access_token-test'
    )
    licong_test = forms.CharField(
        max_length=255,
        help_text='这是我测试的'
    )
