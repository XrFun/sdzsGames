/**
 * Created by youmo on 2017/2/17.
 */

var GameConst = GameConst || {};

GameConst.NormalBtnSkin =
    `<e:Skin class="skins.ButtonSkin" states="up,down,disabled" minHeight="50" minWidth="100" xmlns:e="http://ns.egret.com/eui">
                <e:Image width="100%" height="100%" scale9Grid="1,3,8,8" alpha.disabled="0.5"
                         source="resource/button/button_up.png"
                         source.down="resource/button/button_down.png"/>
                <e:Label id="labelDisplay" top="8" bottom="8" left="8" right="8"
                         textColor="0xFFFFFF" verticalAlign="middle" textAlign="center"/>
                <e:Image id="iconDisplay" horizontalCenter="0" verticalCenter="0"/>
            </e:Skin>`;


//GameConst.MaxWidth = egret.MainContext.instance.stage.stageWidth;
//GameConst.MaxHeight = egret.MainContext.instance.stage.stageHeight;