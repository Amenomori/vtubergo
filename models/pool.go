package models

import (
	"fmt"
)

type Pool struct {
	Msg chan Message
}

func NewPool() *Pool {
	return &Pool{
		Msg: make(chan Message, 10),
	}
}

func (pool *Pool) Handle() {
	for {
		src := <-pool.Msg
		//log.Println(src)
		switch src.Cmd {
		case CMDInteractWord:
			continue
		case CMDDanmuMsg:
			continue
		case CMDEntry:
			continue
		case CMDWelcome:
			fmt.Println(src)
		case CMDWelcomeGuard:
			fmt.Println(src)
		case CMDSendGift:
			continue
		case CMDComboSend:
			continue
		case CMDSuperChatMessage:
			continue
		case CMDSuperChatMessageJpn:
			continue
		case CMDOnlineRankV2:
			continue
		case CMDOnlineRankCount:
			continue
		case CMDRoomRealTimeMessageUpdate:
			continue
		case CMDHotRankChanged:
			continue
		case CMDWidgetBanner:
			continue
		case CMDNoticeMsg:
			continue
		default:
			fmt.Println(src)
		}
	}
}
