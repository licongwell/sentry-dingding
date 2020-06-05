# coding: utf-8
ignore_regular = '错误d信息啊'
highest_level_regular = 'ksobe'
medium_level_regular = 'james'
low_level_regular = 'wade'
fix_project_name = "自定义项目名字"
isNeedAtAll = False

cc = False
if not cc :
  print('12212')
else:
  print("dsadsa")  

message = "这是我的kobe错误信息啊，james这个是怎么个意思呢"

firstScreenTitle = "这是钉钉的展示缩略信息"
contentTitle = "这是钉钉消息正式消息里面的title"

resultDingStrObj = {}

print(bool('dsa'))

class FilterErrorLevel:
  def checkMessage (self):
    isIgnoreMessage = self.regularInMessage(ignore_regular)
    isHighLevel = self.regularInMessage(highest_level_regular)
    isMediumLevel = self.regularInMessage(medium_level_regular)
    isLowLevel = self.regularInMessage(low_level_regular)

    if isIgnoreMessage:
      print("匹配到了需要忽略的信息了")
      return False

    if isHighLevel:      
      resultDingStrObj["firstScreenTitle"] = "【高危错误!!请及时处理】来自"+ fix_project_name
      resultDingStrObj["contentTitle"] = "**【高危】错误信息**来自"+fix_project_name
      resultDingStrObj["isNeedAtAll"] = True
      return resultDingStrObj

    if isMediumLevel:
      resultDingStrObj["firstScreenTitle"] = "【中危错误!】来自"+ fix_project_name
      resultDingStrObj["contentTitle"] = "**【中危】错误信息**来自"+fix_project_name
      return resultDingStrObj

    if isLowLevel:
      resultDingStrObj["firstScreenTitle"] = "【低危错误】来自"+ fix_project_name
      resultDingStrObj["contentTitle"] = "【低危】错误信息来自"+fix_project_name
      return resultDingStrObj

    resultDingStrObj["firstScreenTitle"] = "New error from"+ fix_project_name
    resultDingStrObj["contentTitle"] = "New error from"+ fix_project_name
    return resultDingStrObj


  def regularInMessage (self, inputSrt):
    if (bool(inputSrt)):
      strArr = inputSrt.split("||") 
      for item in strArr:
        if item in message:
          return True
    else:
      return False       

cc = FilterErrorLevel()
aa = cc.checkMessage()
print aa["contentTitle"]
