from botoy import Botoy, GroupMsg, FriendMsg, Action
from botoy import decorators as deco
from
import os
import configparser
bot = Botoy(qq=723205471, log_file=True)
action = Action(qq=723205471, port=8888, host='localhost')



@bot.on_friend_msg
@deco.ensure_tempMsg
@deco.ignore_botself
@deco.equal_content("初始化")
def init(ctx: FriendMsg):
    if not os.path.exists("config"):
        os.mkdir("config")
    group_list = action.getGroupList()
    for group in group_list:



@bot.on_group_msg
@deco.equal_content("更新群列表")
def refresh_group_list(ctx: GroupMsg):
    group_list = action.getGroupList()
    groupList = list()


    action.sendGroupText(ctx.FromGroupId, "当前加入群聊：" + str(groupList))

if __name__ == '__main__':
    bot.run()

