import os
import json

null = None
false = False
true = True

json1 = [{"cmd":"COMBO_SEND","data":{"uid":316320811,"ruid":7706705,"uname":"嘉然明天吃阿草","r_uname":"阿梓从小就很可爱","combo_num":28,"gift_id":30607,"gift_num":0,"batch_combo_num":28,"gift_name":"小心心","action":"投喂","combo_id":"gift:combo_id:316320811:7706705:30607:1619791333.7220","batch_combo_id":"batch:gift:combo_id:316320811:7706705:30607:1619791345.3528","is_show":1,"send_master":null,"name_color":"","total_num":28,"medal_info":{"target_id":672328094,"special":"","icon_id":0,"anchor_uname":"","anchor_roomid":0,"medal_level":23,"medal_name":"嘉心糖","medal_color":1725515,"medal_color_start":1725515,"medal_color_end":5414290,"medal_color_border":6809855,"is_lighted":1,"guard_level":3},"combo_total_coin":0}}]

json2 = [{"cmd":"SUPER_CHAT_MESSAGE_JPN","data":{"id":"1659828","uid":"13817659","price":50,"rate":1000,"message":"\u4e0d\u4f1a\u521d\u97f3\u672a\u6765\uff1f\u4e0d\u4f1a\u521d\u97f3\u672a\u6765\uff1f\u90a3\u672c\u4e8c\u6b21\u5143\u6211\u53ea\u80fd\u8bf4\u6ca1\u6709\u542b\u91d1\u91cf\u4e86","message_jpn":"\u521d\u97f3\u30df\u30af\u3067\u304d\u306a\u3044\uff1f\u521d\u97f3\u30df\u30af\u3067\u304d\u306a\u3044\uff1f\u305d\u306e\u4e8c\u6b21\u5143\u306f\u304a\u91d1\u306e\u91cf\u304c\u306a\u3044\u3068\u3057\u304b\u8a00\u3044\u3088\u3046\u304c\u306a\u3044\u3067\u3059\u3002","is_ranked":1,"background_image":"https:\/\/i0.hdslb.com\/bfs\/live\/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_color":"#DBFFFD","background_icon":"","background_price_color":"#7DA4BD","background_bottom_color":"#427D9E","ts":1619792270,"token":"AAB4072A","medal_info":{"icon_id":0,"target_id":672328094,"special":"","anchor_uname":"\u5609\u7136\u4eca\u5929\u5403\u4ec0\u4e48","anchor_roomid":22637261,"medal_level":10,"medal_name":"\u5609\u5fc3\u7cd6","medal_color":"#8d7ca6"},"user_info":{"uname":"\u5609\u7136\u4eca\u5929\u5403\u732b\u732b","face":"http:\/\/i1.hdslb.com\/bfs\/face\/ffac951eb11b32b65215f2a6a7982e8e4ea8186b.jpg","face_frame":"","guard_level":0,"user_level":20,"level_color":"#61c05a","is_vip":0,"is_svip":0,"is_main_vip":1,"title":"0","manager":0},"time":119,"start_time":1619792270,"end_time":1619792390,"gift":{"num":1,"gift_id":12000,"gift_name":"\u9192\u76ee\u7559\u8a00"}},"roomid":"23028000"}]

json3 = [{"cmd":"SUPER_CHAT_MESSAGE","data":{"id":1659828,"uid":13817659,"price":50,"rate":1000,"message":"不会初音未来？不会初音未来？那本二次元我只能说没有含金量了","trans_mark":1,"is_ranked":1,"message_trans":"初音ミクできない？初音ミクできない？その二次元はお金の量がないとしか言いようがないです。","background_color_start":"#4EA4C5","background_color_end":"#29718B","color_point":0.7,"message_font_color":"#A3F6FF","background_image":"https://i0.hdslb.com/bfs/live/a712efa5c6ebc67bafbe8352d3e74b820a00c13e.png","background_color":"#DBFFFD","background_icon":"","background_price_color":"#7DA4BD","background_bottom_color":"#427D9E","ts":1619792270,"is_send_audit":"0","token":"AAB4072A","medal_info":{"icon_id":0,"target_id":672328094,"special":"","anchor_uname":"嘉然今天吃什么","anchor_roomid":22637261,"medal_level":10,"medal_name":"嘉心糖","medal_color":"#8d7ca6","medal_color_start":9272486,"medal_color_end":9272486,"medal_color_border":9272486,"is_lighted":1,"guard_level":0},"user_info":{"uname":"嘉然今天吃猫猫","face":"http://i1.hdslb.com/bfs/face/ffac951eb11b32b65215f2a6a7982e8e4ea8186b.jpg","face_frame":"","name_color":"#666666","guard_level":0,"user_level":20,"level_color":"#61c05a","is_vip":0,"is_svip":0,"is_main_vip":1,"title":"0","manager":0},"time":120,"start_time":1619792270,"end_time":1619792390,"gift":{"num":1,"gift_id":12000,"gift_name":"醒目留言"}},"roomid":"23028000"}]

json4 = [{"cmd":"ROOM_REAL_TIME_MESSAGE_UPDATE","data":{"roomid":21449083,"fans":390641,"red_notice":-1,"fans_club":7844}}]

json5 = [{"cmd":"INTERACT_WORD","data":{"uid":2996627,"uname":"人活着就是为了阎魔爱","uname_color":"","identities":[3,1],"msg_type":1,"roomid":6374209,"timestamp":1619849425,"score":1619908686379,"fans_medal":{"target_id":1492,"medal_level":14,"medal_name":"Q老板","medal_color":12478086,"medal_color_start":12478086,"medal_color_end":12478086,"medal_color_border":12478086,"is_lighted":1,"guard_level":0,"special":"","icon_id":0,"anchor_roomid":1022,"score":49261},"is_spread":0,"spread_info":"","contribution":{"grade":0},"spread_desc":"","tail_icon":0}}]

json6 = [{"cmd":"DANMU_MSG","info":[[0,1,25,16777215,1619850081987,345757085,0,"94d2ed55",0,0,0,""],"我回来了",[1248910347,"生活自己舒服就好",0,0,0,10000,1,""],[],[0,0,9868950,"\u003e50000",0],["",""],0,0,null,{"ts":1619850081,"ct":"FD26AF25"},0,0,null,null,0]}]

json7 = [{"cmd":"SEND_GIFT","data":{"draw":0,"gold":0,"silver":0,"num":1,"total_coin":0,"effect":0,"broadcast_id":0,"crit_prob":0,"guard_level":0,"rcost":69772475,"uid":8499240,"timestamp":1619851137,"giftId":30607,"giftType":5,"super":0,"super_gift_num":2,"super_batch_gift_num":2,"remain":0,"price":0,"beatId":"0","biz_source":"Live","action":"投喂","coin_type":"silver","uname":"雨森_Rie","face":"http://i0.hdslb.com/bfs/face/37c11c6715c5b69651040eb9d9bbfc04dcf53c0a.jpg","batch_combo_id":"batch:gift:combo_id:8499240:14387072:30607:1619851136.6066","rnd":"1619851067","giftName":"小心心","original_gift_name":"","combo_send":null,"batch_combo_send":null,"tag_image":"","top_list":null,"send_master":null,"is_first":false,"demarcation":1,"combo_stay_time":3,"combo_total_coin":1,"tid":"1619851137110000001","effect_block":1,"is_special_batch":0,"combo_resources_id":1,"magnification":1,"name_color":"","medal_info":{"target_id":271887040,"special":"","icon_id":0,"anchor_uname":"","anchor_roomid":0,"medal_level":2,"medal_name":"爱讨论","medal_color":6067854,"medal_color_start":6067854,"medal_color_end":6067854,"medal_color_border":6067854,"is_lighted":1,"guard_level":0},"svga_block":0,"blind_gift":null}}]

json8 = [{"cmd":"SEND_GIFT","data":{"action":"投喂","batch_combo_id":"batch:gift:combo_id:8499240:14387072:30607:1619851136.6066","batch_combo_send":null,"beatId":"0","biz_source":"Live","blind_gift":null,"broadcast_id":0,"coin_type":"silver","combo_resources_id":1,"combo_send":null,"combo_stay_time":3,"combo_total_coin":1,"crit_prob":0,"demarcation":1,"dmscore":8,"draw":0,"effect":0,"effect_block":1,"face":"http://i0.hdslb.com/bfs/face/37c11c6715c5b69651040eb9d9bbfc04dcf53c0a.jpg","giftId":30607,"giftName":"小心心","giftType":5,"gold":0,"guard_level":0,"is_first":true,"is_special_batch":0,"magnification":1,"medal_info":{"anchor_roomid":0,"anchor_uname":"","guard_level":0,"icon_id":0,"is_lighted":1,"medal_color":6067854,"medal_color_border":6067854,"medal_color_end":6067854,"medal_color_start":6067854,"medal_level":2,"medal_name":"爱讨论","special":"","target_id":271887040},"name_color":"","num":1,"original_gift_name":"","price":0,"rcost":69772475,"remain":1,"rnd":"1619851067","send_master":null,"silver":0,"super":0,"super_batch_gift_num":1,"super_gift_num":1,"svga_block":0,"tag_image":"","tid":"1619851136110000001","timestamp":1619851136,"top_list":null,"total_coin":0,"uid":8499240,"uname":"雨森_Rie"}}]

json9 = [{"cmd":"ONLINE_RANK_V2","data":{"list":[{"uid":14974284,"face":"http://i0.hdslb.com/bfs/face/eb97ecc3d2d183e11fc7028222d74a8e1a53e84f.jpg","score":"1380","uname":"暮光云宝","rank":1,"guard_level":3},{"uid":9978105,"face":"http://i0.hdslb.com/bfs/face/71bc52ecf1d22273fb2cfb0f7381e4aa9a317046.jpg","score":"1001","uname":"废物进儿","rank":2,"guard_level":3},{"uid":15576675,"face":"http://i0.hdslb.com/bfs/face/8fd7bf11f16ae01d0be6948187db573598142272.jpg","score":"900","uname":"绝唱小蜻蜓","rank":3,"guard_level":3},{"uid":39496612,"face":"http://i1.hdslb.com/bfs/face/685d8ca6b6e90ae71052ced78793a4374a9e7431.jpg","score":"99","uname":"袭风披云","rank":4,"guard_level":0},{"uid":14672989,"face":"http://i1.hdslb.com/bfs/face/852a63ebf2eb4715a0cc040691659fb4a8732902.jpg","score":"90","uname":"柯基小奶狗","rank":5,"guard_level":2},{"uid":387819883,"face":"http://i1.hdslb.com/bfs/face/081b2f06acc8ce9a8c4c4ab14a75bdaae5a598e5.jpg","score":"10","uname":"紫龙馨","rank":6,"guard_level":0},{"uid":113169,"face":"http://i0.hdslb.com/bfs/face/d245ab9d8004ddf2f26bcdbada67b89f24fe56ac.gif","score":"9","uname":"阿梓De七月","rank":7,"guard_level":0}],"rank_type":"gold-rank"}}]

json10 = [{"cmd":"ONLINE_RANK_COUNT","data":{"count":7}}]

json11 = [{"cmd":"ONLINE_RANK_TOP3","data":{"list":[{"msg":"恭喜 \u003c%绝唱小蜻蜓%\u003e 成为高能榜","rank":3}]}}]

json12 = [{"cmd":"ENTRY_EFFECT","data":{"id":4,"uid":173495753,"target_id":14387072,"mock_effect":0,"face":"https://i2.hdslb.com/bfs/face/98c1ab95b8330364f69952e06f4e9135a1751f1a.jpg","privilege_type":3,"copy_writing":"欢迎舰长 \u003c%机铠种千成%\u003e 进入直播间","copy_color":"#ffffff","highlight_color":"#E6FF00","priority":1,"basemap_url":"https://i0.hdslb.com/bfs/live/mlive/f34c7441cdbad86f76edebf74e60b59d2958f6ad.png","show_avatar":1,"effective_time":2,"web_basemap_url":"","web_effective_time":0,"web_effect_close":0,"web_close_time":0,"business":1,"copy_writing_v2":"欢迎舰长 \u003c%机铠种千成%\u003e 进入直播间","icon_list":[],"max_delay_time":7}}]

json13 = [{"cmd":"HOT_RANK_CHANGED","data":{"rank":26,"trend":1,"countdown":1240,"timestamp":1619852960,"web_url":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=2\u0026area_id=9","live_url":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=1\u0026area_id=9\u0026is_live_half_webview=1\u0026hybrid_rotate_d=1\u0026is_cling_player=1\u0026hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0","blink_url":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=3\u0026area_id=9\u0026is_live_half_webview=1\u0026hybrid_rotate_d=1\u0026is_cling_player=1\u0026hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0","live_link_url":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=5\u0026area_id=9\u0026is_live_half_webview=1\u0026hybrid_rotate_d=1\u0026is_cling_player=1\u0026hybrid_half_ui=1,3,100p,70p,f4eefa,0,30,100,0,0;2,2,375,100p,f4eefa,0,30,100,0,0;3,3,100p,70p,f4eefa,0,30,100,0,0;4,2,375,100p,f4eefa,0,30,100,0,0;5,3,100p,70p,f4eefa,0,30,100,0,0;6,3,100p,70p,f4eefa,0,30,100,0,0;7,3,100p,70p,f4eefa,0,30,100,0,0;8,3,100p,70p,f4eefa,0,30,100,0,0","pc_link_url":"https://live.bilibili.com/p/html/live-app-hotrank/index.html?clientType=4\u0026is_live_half_webview=1\u0026area_id=9\u0026pc_ui=338,465,f4eefa,0","icon":"https://i0.hdslb.com/bfs/live/63217712edb588864b2c714225992e7f46b0b917.png","area_name":"虚拟"}}]

json14 = [{"cmd":"WIDGET_BANNER","data":{"timestamp":1619852970,"widget_list":{"42":{"id":42,"title":"五一初夏美味赏","cover":"","tip_text":"初夏美味赏","tip_text_color":"#EDF1F2","tip_bottom_color":"#00B2FF","jump_url":"https://live.bilibili.com/activity/live-activity-battle/index.html?is_live_half_webview=1\u0026hybrid_rotate_d=1\u0026is_cling_player=1\u0026hybrid_half_ui=1,3,100p,70p,a27af6,0,30,100;2,2,375,100p,a27af6,0,30,100;3,3,100p,70p,a27af6,0,30,100;4,2,375,100p,a27af6,0,30,100;5,3,100p,70p,a27af6,0,30,100;6,3,100p,70p,a27af6,0,30,100;7,3,100p,70p,a27af6,0,30,100;8,3,100p,70p,a27af6,0,30,100\u0026room_id=918717\u0026uid=2341174#/may_day_holiday","url":"","stay_time":6,"site":1,"platform_in":["live","blink","live_link","web","pc_link"],"type":1,"band_id":12001,"sub_key":"","sub_data":"%7B%22show_type%22%3A4%2C%22rank_info%22%3A%7B%22nickname%22%3A%22%22%2C%22user_face%22%3A%22%22%7D%2C%22fans_medal%22%3A%7B%22medal_type%22%3A0%2C%22expire_time%22%3A0%2C%22now_time%22%3A1619852967%7D%2C%22task_info%22%3A%7B%22level%22%3A3%2C%22gift_info%22%3A%5B%7B%22gift_id%22%3A30883%2C%22gift_name%22%3A%22%E7%94%9C%E8%9C%9C%E7%B3%96%E6%9E%9C%22%2C%22target%22%3A1%2C%22has_get%22%3A1%2C%22image_url%22%3A%22https%3A%2F%2Fs1.hdslb.com%2Fbfs%2Flive%2Ff3346fa4835425962ba0c29c3a1c1e23f4ab6e8c.png%22%7D%2C%7B%22gift_id%22%3A30885%2C%22gift_name%22%3A%22%E6%B8%85%E5%87%89%E5%88%A8%E5%86%B0%22%2C%22target%22%3A1%2C%22has_get%22%3A0%2C%22image_url%22%3A%22https%3A%2F%2Fs1.hdslb.com%2Fbfs%2Flive%2Fbb749294ca18e7b0ce8248b8aa4fd0d39d5bc33c.png%22%7D%5D%7D%7D","is_add":true}}}}]

json15 = [{"cmd":"NOTICE_MSG","id":2,"name":"分区道具抽奖广播样式","full":{"head_icon":"http://i0.hdslb.com/bfs/live/00f26756182b2e9d06c00af23001bc8e10da67d0.webp","tail_icon":"http://i0.hdslb.com/bfs/live/822da481fdaba986d738db5d8fd469ffa95a8fa1.webp","head_icon_fa":"http://i0.hdslb.com/bfs/live/77983005023dc3f31cd599b637c83a764c842f87.png","tail_icon_fa":"http://i0.hdslb.com/bfs/live/38cb2a9f1209b16c0f15162b0b553e3b28d9f16f.png","head_icon_fan":36,"tail_icon_fan":4,"background":"#6098FFFF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":20},"half":{"head_icon":"http://i0.hdslb.com/bfs/live/358cc52e974b315e83eee429858de4fee97a1ef5.png","tail_icon":"","background":"#7BB6F2FF","color":"#FFFFFFFF","highlight":"#FDFF2FFF","time":15},"side":{"head_icon":"","background":"","color":"","highlight":"","border":""},"roomid":23045312,"real_roomid":23045312,"msg_common":"\u003c%风涌而至%\u003e投喂:\u003c%茨少凌_Channel%\u003e1个摩天大楼，点击前往TA的房间吧！","msg_self":"\u003c%风涌而至%\u003e投喂:\u003c%茨少凌_Channel%\u003e1个摩天大楼，快来吧！","link_url":"https://live.bilibili.com/23045312?accept_quality=%5B4%5D\u0026broadcast_type=0\u0026current_qn=10000\u0026current_quality=10000\u0026extra_jump_from=28003\u0026from=28003\u0026is_room_feed=0\u0026live_lottery_type=1\u0026live_play_network=other\u0026p2p_type=0\u0026playurl_h264=http%3A%2F%2Fd1--cn-gotcha05.bilivideo.com%2Flive-bvc%2F999655%2Flive_436823223_52253960.flv%3Fcdn%3Dcn-gotcha05%26expires%3D1619856923%26len%3D0%26oi%3D0%26pt%3D%26qn%3D10000%26trid%3D65e98a6ca07449cab585300f259e7820%26sigparams%3Dcdn%2Cexpires%2Clen%2Coi%2Cpt%2Cqn%2Ctrid%26sign%3D591a3f1ccc8a9c0f77e8fda77484a4d6%26ptype%3D0%26src%3D8%26sl%3D1%26sk%3D87af7c4a512d23a%26order%3D1\u0026playurl_h265=\u0026quality_description=%5B%7B%22qn%22%3A10000%2C%22desc%22%3A%22%E5%8E%9F%E7%94%BB%22%7D%5D","msg_type":2,"shield_uid":-1,"business_id":"20003","scatter":{"min":0,"max":0}}]

print(json1+json2+json3+json4+json5+json6+json7+json8+
      json9+json10+json11+json12+json13+json14+json15)
