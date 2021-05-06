package models

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"github.com/gorilla/websocket"
	"log"
	"time"
)

var (
	CMDDanmuMsg                  = "DANMU_MSG"                     // 普通弹幕信息
	CMDSendGift                  = "SEND_GIFT"                     // 普通的礼物，不包含礼物连击
	CMDComboSend                 = "COMBO_SEND"                    // 连击礼物
	CMDWelcome                   = "WELCOME"                       // 欢迎VIP
	CMDWelcomeGuard              = "WELCOME_GUARD"                 // 欢迎房管
	CMDEntry                     = "ENTRY_EFFECT"                  // 欢迎舰长等头衔
	CMDRoomRealTimeMessageUpdate = "ROOM_REAL_TIME_MESSAGE_UPDATE" // 房间关注数变动
	CMDSuperChatMessage          = "SUPER_CHAT_MESSAGE"            // SC
	CMDSuperChatMessageJpn       = "SUPER_CHAT_MESSAGE_JPN"        // SC(JPN)
	CMDInteractWord              = "INTERACT_WORD"
	CMDOnlineRankV2              = "ONLINE_RANK_V2"
	CMDOnlineRankCount           = "ONLINE_RANK_COUNT"
	CMDHotRankChanged            = "HOT_RANK_CHANGED"
	CMDWidgetBanner              = "WIDGET_BANNER"
	CMDNoticeMsg                 = "NOTICE_MSG"
)

type Message struct {
	Cmd  string `json:"cmd"`
	Data struct {
		Uid           interface{} `json:"uid,omitempty"`
		Ruid          int         `json:"ruid,omitempty"`
		Uname         string      `json:"uname,omitempty"`
		RUname        string      `json:"r_uname,omitempty"`
		ComboNum      int         `json:"combo_num,omitempty"`
		GiftId        int         `json:"gift_id,omitempty"`
		GiftNum       int         `json:"gift_num,omitempty"`
		BatchComboNum int         `json:"batch_combo_num,omitempty"`
		GiftName      string      `json:"gift_name,omitempty"`
		Action        string      `json:"action,omitempty"`
		ComboId       string      `json:"combo_id,omitempty"`
		BatchComboId  string      `json:"batch_combo_id,omitempty"`
		IsShow        int         `json:"is_show,omitempty"`
		SendMaster    interface{} `json:"send_master,omitempty"`
		NameColor     string      `json:"name_color,omitempty"`
		TotalNum      int         `json:"total_num,omitempty"`
		MedalInfo     struct {
			TargetId         int         `json:"target_id"`
			Special          string      `json:"special"`
			IconId           int         `json:"icon_id"`
			AnchorUname      string      `json:"anchor_uname"`
			AnchorRoomid     int         `json:"anchor_roomid"`
			MedalLevel       int         `json:"medal_level"`
			MedalName        string      `json:"medal_name"`
			MedalColor       interface{} `json:"medal_color"`
			MedalColorStart  int         `json:"medal_color_start,omitempty"`
			MedalColorEnd    int         `json:"medal_color_end,omitempty"`
			MedalColorBorder int         `json:"medal_color_border,omitempty"`
			IsLighted        int         `json:"is_lighted,omitempty"`
			GuardLevel       int         `json:"guard_level,omitempty"`
		} `json:"medal_info,omitempty"`
		ComboTotalCoin        int         `json:"combo_total_coin,omitempty"`
		Id                    interface{} `json:"id,omitempty"`
		Price                 int         `json:"price,omitempty"`
		Rate                  int         `json:"rate,omitempty"`
		Message               string      `json:"message,omitempty"`
		MessageJpn            string      `json:"message_jpn,omitempty"`
		IsRanked              int         `json:"is_ranked,omitempty"`
		BackgroundImage       string      `json:"background_image,omitempty"`
		BackgroundColor       string      `json:"background_color,omitempty"`
		BackgroundIcon        string      `json:"background_icon,omitempty"`
		BackgroundPriceColor  string      `json:"background_price_color,omitempty"`
		BackgroundBottomColor string      `json:"background_bottom_color,omitempty"`
		Ts                    int         `json:"ts,omitempty"`
		Token                 string      `json:"token,omitempty"`
		UserInfo              struct {
			Uname      string `json:"uname"`
			Face       string `json:"face"`
			FaceFrame  string `json:"face_frame"`
			GuardLevel int    `json:"guard_level"`
			UserLevel  int    `json:"user_level"`
			LevelColor string `json:"level_color"`
			IsVip      int    `json:"is_vip"`
			IsSvip     int    `json:"is_svip"`
			IsMainVip  int    `json:"is_main_vip"`
			Title      string `json:"title"`
			Manager    int    `json:"manager"`
			NameColor  string `json:"name_color,omitempty"`
		} `json:"user_info,omitempty"`
		Time      int `json:"time,omitempty"`
		StartTime int `json:"start_time,omitempty"`
		EndTime   int `json:"end_time,omitempty"`
		Gift      struct {
			Num      int    `json:"num"`
			GiftId   int    `json:"gift_id"`
			GiftName string `json:"gift_name"`
		} `json:"gift,omitempty"`
		TransMark            int     `json:"trans_mark,omitempty"`
		MessageTrans         string  `json:"message_trans,omitempty"`
		BackgroundColorStart string  `json:"background_color_start,omitempty"`
		BackgroundColorEnd   string  `json:"background_color_end,omitempty"`
		ColorPoint           float64 `json:"color_point,omitempty"`
		MessageFontColor     string  `json:"message_font_color,omitempty"`
		IsSendAudit          string  `json:"is_send_audit,omitempty"`
		Roomid               int     `json:"roomid,omitempty"`
		Fans                 int     `json:"fans,omitempty"`
		RedNotice            int     `json:"red_notice,omitempty"`
		FansClub             int     `json:"fans_club,omitempty"`
		UnameColor           string  `json:"uname_color,omitempty"`
		Identities           []int   `json:"identities,omitempty"`
		MsgType              int     `json:"msg_type,omitempty"`
		Timestamp            int     `json:"timestamp,omitempty"`
		Score                int64   `json:"score,omitempty"`
		FansMedal            struct {
			TargetId         int    `json:"target_id"`
			MedalLevel       int    `json:"medal_level"`
			MedalName        string `json:"medal_name"`
			MedalColor       int    `json:"medal_color"`
			MedalColorStart  int    `json:"medal_color_start"`
			MedalColorEnd    int    `json:"medal_color_end"`
			MedalColorBorder int    `json:"medal_color_border"`
			IsLighted        int    `json:"is_lighted"`
			GuardLevel       int    `json:"guard_level"`
			Special          string `json:"special"`
			IconId           int    `json:"icon_id"`
			AnchorRoomid     int    `json:"anchor_roomid"`
			Score            int    `json:"score"`
		} `json:"fans_medal,omitempty"`
		IsSpread     int    `json:"is_spread,omitempty"`
		SpreadInfo   string `json:"spread_info,omitempty"`
		Contribution struct {
			Grade int `json:"grade"`
		} `json:"contribution,omitempty"`
		SpreadDesc        string      `json:"spread_desc,omitempty"`
		TailIcon          int         `json:"tail_icon,omitempty"`
		Draw              int         `json:"draw,omitempty"`
		Gold              int         `json:"gold,omitempty"`
		Silver            int         `json:"silver,omitempty"`
		Num               int         `json:"num,omitempty"`
		TotalCoin         int         `json:"total_coin,omitempty"`
		Effect            int         `json:"effect,omitempty"`
		BroadcastId       int         `json:"broadcast_id,omitempty"`
		CritProb          int         `json:"crit_prob,omitempty"`
		GuardLevel        int         `json:"guard_level,omitempty"`
		Rcost             int         `json:"rcost,omitempty"`
		GiftId1           int         `json:"giftId,omitempty"`
		GiftType          int         `json:"giftType,omitempty"`
		Super             int         `json:"super,omitempty"`
		SuperGiftNum      int         `json:"super_gift_num,omitempty"`
		SuperBatchGiftNum int         `json:"super_batch_gift_num,omitempty"`
		Remain            int         `json:"remain,omitempty"`
		BeatId            string      `json:"beatId,omitempty"`
		BizSource         string      `json:"biz_source,omitempty"`
		CoinType          string      `json:"coin_type,omitempty"`
		Face              string      `json:"face,omitempty"`
		Rnd               string      `json:"rnd,omitempty"`
		GiftName1         string      `json:"giftName,omitempty"`
		OriginalGiftName  string      `json:"original_gift_name,omitempty"`
		ComboSend         interface{} `json:"combo_send,omitempty"`
		BatchComboSend    interface{} `json:"batch_combo_send,omitempty"`
		TagImage          string      `json:"tag_image,omitempty"`
		TopList           interface{} `json:"top_list,omitempty"`
		IsFirst           interface{} `json:"is_first,omitempty"`
		Demarcation       int         `json:"demarcation,omitempty"`
		ComboStayTime     int         `json:"combo_stay_time,omitempty"`
		Tid               string      `json:"tid,omitempty"`
		EffectBlock       int         `json:"effect_block,omitempty"`
		IsSpecialBatch    int         `json:"is_special_batch,omitempty"`
		ComboResourcesId  int         `json:"combo_resources_id,omitempty"`
		Magnification     int         `json:"magnification,omitempty"`
		SvgaBlock         int         `json:"svga_block,omitempty"`
		BlindGift         interface{} `json:"blind_gift,omitempty"`
		Dmscore           int         `json:"dmscore,omitempty"`
		List              []struct {
			Uid        int    `json:"uid,omitempty"`
			Face       string `json:"face,omitempty"`
			Score      string `json:"score,omitempty"`
			Uname      string `json:"uname,omitempty"`
			Rank       int    `json:"rank"`
			GuardLevel int    `json:"guard_level,omitempty"`
			Msg        string `json:"msg,omitempty"`
		} `json:"list,omitempty"`
		RankType         string        `json:"rank_type,omitempty"`
		Count            int           `json:"count,omitempty"`
		TargetId         int           `json:"target_id,omitempty"`
		MockEffect       int           `json:"mock_effect,omitempty"`
		PrivilegeType    int           `json:"privilege_type,omitempty"`
		CopyWriting      string        `json:"copy_writing,omitempty"`
		CopyColor        string        `json:"copy_color,omitempty"`
		HighlightColor   string        `json:"highlight_color,omitempty"`
		Priority         int           `json:"priority,omitempty"`
		BasemapUrl       string        `json:"basemap_url,omitempty"`
		ShowAvatar       int           `json:"show_avatar,omitempty"`
		EffectiveTime    int           `json:"effective_time,omitempty"`
		WebBasemapUrl    string        `json:"web_basemap_url,omitempty"`
		WebEffectiveTime int           `json:"web_effective_time,omitempty"`
		WebEffectClose   int           `json:"web_effect_close,omitempty"`
		WebCloseTime     int           `json:"web_close_time,omitempty"`
		Business         int           `json:"business,omitempty"`
		CopyWritingV2    string        `json:"copy_writing_v2,omitempty"`
		IconList         []interface{} `json:"icon_list,omitempty"`
		MaxDelayTime     int           `json:"max_delay_time,omitempty"`
		Rank             int           `json:"rank,omitempty"`
		Trend            int           `json:"trend,omitempty"`
		Countdown        int           `json:"countdown,omitempty"`
		WebUrl           string        `json:"web_url,omitempty"`
		LiveUrl          string        `json:"live_url,omitempty"`
		BlinkUrl         string        `json:"blink_url,omitempty"`
		LiveLinkUrl      string        `json:"live_link_url,omitempty"`
		PcLinkUrl        string        `json:"pc_link_url,omitempty"`
		Icon             string        `json:"icon,omitempty"`
		AreaName         string        `json:"area_name,omitempty"`
		WidgetList       struct {
			Field1 struct {
				Id             int         `json:"id"`
				Title          string      `json:"title"`
				Cover          string      `json:"cover"`
				TipText        string      `json:"tip_text"`
				TipTextColor   string      `json:"tip_text_color"`
				TipBottomColor string      `json:"tip_bottom_color"`
				JumpUrl        string      `json:"jump_url"`
				Url            string      `json:"url"`
				StayTime       int         `json:"stay_time"`
				Site           int         `json:"site"`
				PlatformIn     []string    `json:"platform_in"`
				Type           int         `json:"type"`
				BandId         int         `json:"band_id"`
				SubKey         string      `json:"sub_key"`
				SubData        string      `json:"sub_data"`
				IsAdd          interface{} `json:"is_add"`
			} `json:"42"`
		} `json:"widget_list,omitempty"`
	} `json:"data,omitempty"`
	Roomid string        `json:"roomid,omitempty"`
	Info   []interface{} `json:"info,omitempty"`
}

func (c *Client) SendPackage(packetlen uint32, magic uint16, ver uint16, typeID uint32, param uint32, data []byte) (err error) {
	packetHead := new(bytes.Buffer)

	if packetlen == 0 {
		packetlen = uint32(len(data) + 16)
	}
	var pdata = []interface{}{
		packetlen,
		magic,
		ver,
		typeID,
		param,
	}

	// 将包的头部信息以大端序方式写入字节数组
	for _, v := range pdata {
		if err = binary.Write(packetHead, binary.BigEndian, v); err != nil {
			fmt.Println("binary.Write err: ", err)
			return
		}
	}

	// 将包内数据部分追加到数据包内
	sendData := append(packetHead.Bytes(), data...)

	// fmt.Println("本次发包消息为：", sendData)

	if err = c.Conn.WriteMessage(websocket.BinaryMessage, sendData); err != nil {
		fmt.Println("c.conn.Write err: ", err)
		return
	}

	return
}

func (c *Client) ReceiveMsg() {
	pool := NewPool()
	go pool.Handle()
	for {
		_, msg, err := c.Conn.ReadMessage()
		if err != nil {
			log.Println("ReadMsg err :", err)
			continue
		}

		switch msg[11] {
		case 8:
			fmt.Println("握手包收发完毕，连接成功")
			c.Connected = true
		case 3:
			onlineNow := ByteArrToDecimal(msg[16:])
			if uint32(onlineNow) != c.Room.Online {
				c.Room.Online = uint32(onlineNow)
				log.Println("当前房间人气变动：", uint32(onlineNow))
			}
		case 5:
			if inflated, err := ZlibInflate(msg[16:]); err != nil {
				// 代表是未压缩数据
				tempMsg := Message{}
				err = json.Unmarshal(msg[16:], &tempMsg)
				log.Println(string(msg[16:]))
				pool.Msg <- tempMsg
			} else {
				for len(inflated) > 0 {
					l := ByteArrToDecimal(inflated[:4])
					tempMsg := Message{}
					//log.Println(string(inflated[16:l]))
					if err = json.Unmarshal([]byte(inflated[16:l]), &tempMsg); err != nil {
						log.Println("Unmarshal error: ", err)
					}
					pool.Msg <- tempMsg
					inflated = inflated[l:]
				}
			}
		}
	}
}

func (c *Client) HeartBeat() {
	for {
		if c.Connected {
			obj := []byte("5b6f626a656374204f626a6563745d")
			if err := c.SendPackage(0, 16, 1, 2, 1, obj); err != nil {
				log.Println("Heartbeat Error: ", err)
				continue
			}
			time.Sleep(30 * time.Second)
		}
	}
}
