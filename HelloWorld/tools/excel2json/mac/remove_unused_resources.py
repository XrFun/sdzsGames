import os
import sys
import re
import shutil
import time
import plistlib

PROP_NAME_LIST = ['displayFrame', 'normalSpriteFrame', 'selectedSpriteFrame', 'disabledSpriteFrame']
PROP_NAME_LIST.extend(['spriteFrame', 'backgroundSpriteFrame|1', 'backgroundSpriteFrame|2', 'backgroundSpriteFrame|3'])

RESOURCE_EXT = ["png", "jpg"]
PLIST_EXT = ["plist"]
CCBFILE_EXT = ["ccb"]
JS_EXT = ["js"]
SOUNDS_EXT = ["mp3", "wav"]

CURRENT_PATH = os.getcwd()
PROJECT_PATH = os.path.abspath(os.getcwd() + "/../..")

CCBFILES_ROOT_PATH = PROJECT_PATH + "/ccbProject/ccbFiles"
CCBRESOURCE_ROOT_PATH = PROJECT_PATH + "/ccbProject/ccbResources"
CCBPUBLISH_RESOURCE_PATH = PROJECT_PATH + "/ccbPublish/ccbResources"
SRC_ROOT_PATH = PROJECT_PATH + "/src"

RES_PATH = PROJECT_PATH + "/res"
SOUNDS_ROOT_PATH = RES_PATH + "/sounds"


FONT_PATH = CCBRESOURCE_ROOT_PATH + "/fonts"
EFFECT_PATH = CCBRESOURCE_ROOT_PATH + "/effect"
ITEM_CARD_PATH = CCBRESOURCE_ROOT_PATH + "/ui_item_card"

IGNORE_FILE = [FONT_PATH, EFFECT_PATH, ITEM_CARD_PATH]

space_file_list = []
space_pattern = re.compile(r'\s')
digital_pattern = re.compile(r'\d+')

ccb_frame_list = []
all_file_name = []
unused_file_list = []
all_src_dic = {}

TEST_PLIST_PATH = CCBPUBLISH_RESOURCE_PATH + "/resources-iphonehd/ui_common.plist"
TEST_CCB_PATH = CCBFILES_ROOT_PATH + "/effect/match/ballTouchGuide.ccb"

backup_flag = True
BACKUP_PATH = PROJECT_PATH + "/resource_backup"
BACKUP_RECORD_FILE = BACKUP_PATH + "/backup_record.txt"
BACKUP_CCB_PATH = BACKUP_PATH + "/ccbs"
BACKUP_SOUNDS_PATH = BACKUP_PATH + "/sounds"


def createDirectory(path):
    if os.path.exists(path) == False:
        os.mkdir(path)


createDirectory(BACKUP_PATH)
createDirectory(BACKUP_CCB_PATH)
createDirectory(BACKUP_SOUNDS_PATH)



######################## common interface

def isExtFile(file_name, ext):
    file_ext = file_name.split(".")[-1]
    if file_ext in ext:
        return True
    return False


def getFrameName(path):
    sprit_index = path.rfind('/') + 1
    point_index = path.rfind('.')
    if point_index < 1:
        return ""
    return path[sprit_index : point_index]

def getFileName(path):
    start_index = path.rfind('/') + 1
    end_index = len(path)
    return path[start_index : end_index]


def getAllExtFile(dir, ext):
    file_list = []
    if dir in IGNORE_FILE:
        return file_list
    files = os.listdir(dir)
    for file in files:
        file_path = os.path.join(dir, file)
        if os.path.isfile(file_path) and isExtFile(file, ext):
            file_list.append(file_path)
        if os.path.isdir(file_path):
            file_list.extend(getAllExtFile(file_path, ext))
    return file_list

########################


######################## parse file

def parsePlist(plist_file):
    pl = plistlib.readPlist(plist_file)
    return pl.frames.keys()


def parseCCBValue(temp_list):
    for frame in temp_list:
        temp_frame = frame
        if True:
            temp_frame = getFrameName(frame)
        if temp_frame != "" and temp_frame not in ccb_frame_list:
            ccb_frame_list.append(temp_frame)


def parseCCBChildren(children):
    for child in children:
        properties = child.properties
        for prop in properties:
            if prop.name in PROP_NAME_LIST:
                if hasattr(prop, 'baseValue'):
                    parseCCBValue(prop.baseValue)
                parseCCBValue(prop.value)

        if hasattr(child, 'animatedProperties'):
            animatedProperties = child.animatedProperties
            for key in animatedProperties:
                animatedPropertie = animatedProperties[key]
                if hasattr(animatedPropertie, 'displayFrame'):
                    temp_frames = animatedPropertie.displayFrame.keyframes
                    for frame in temp_frames:
                        parseCCBValue(frame.value)

        temp_children = child.children
        if len(temp_children) > 0:
            parseCCBChildren(temp_children)


def parseCCB(ccb_file):
    pc = plistlib.readPlist(ccb_file)
    children = pc.nodeGraph.children

    parseCCBChildren(children)

    ccb_frame_list.sort()

########################

def getAllResourceFile():
    plist_file_list = getAllExtFile(CCBPUBLISH_RESOURCE_PATH, PLIST_EXT)
    resource_list = []
    for file in plist_file_list:
        resource_list.extend(parsePlist(file))

    for item in resource_list:
        match = space_pattern.search(item)
        if match:
            space_file_list.append(item)

    print("space file list count : " + str(len(space_file_list)))
    for item in space_file_list:
        print(item)

    print("resource file count : " + str(len(resource_list)))


def getAllCCBUsedFrame():
    ccb_file_list = getAllExtFile(CCBFILES_ROOT_PATH, CCBFILE_EXT)
    for file in ccb_file_list:
        parseCCB(file)


def getAllFileName():
    file_list = getAllExtFile(CCBRESOURCE_ROOT_PATH, RESOURCE_EXT)

    for file in file_list:
        frame_name = getFrameName(file)
        if digital_pattern.search(frame_name) == None and file not in all_file_name:
            all_file_name.append(file)


def getAllSrcFile():
    file_list = getAllExtFile(SRC_ROOT_PATH, JS_EXT)

    for file in file_list:
        file_object = open(file)
        try:
            all_the_text = file_object.read()
            all_src_dic[file] = all_the_text
        finally:
            file_object.close()

######################## remove image

def checkUnusedFileInCCB():
    for file in all_file_name:
        frame_name = getFrameName(file)
        if frame_name not in ccb_frame_list:
            unused_file_list.append(file)


def checkFrameInDic(frame, dic):
    for key in dic:
        if dic[key].find(frame) != -1:
            return True
    return False

def checkUnusedFileInSrc():
    final_unused_frame = []
    for unused_file in unused_file_list:
        frame_name = getFrameName(unused_file)
        if checkFrameInDic(frame_name, all_src_dic) == False:
            final_unused_frame.append(unused_file)

    if backup_flag == True and os.path.exists(BACKUP_PATH) == False:
        os.mkdir(BACKUP_PATH)

    log_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n"
    log_str += "==== start remove resources...\n"
    for frame in final_unused_frame:
        if backup_flag == True:
            shutil.move(frame, BACKUP_PATH + "/" + getFileName(frame))
        log_str += frame.replace(CCBRESOURCE_ROOT_PATH, "") + "\n"
    log_str += "==== end remove resources... remove count : " + str(len(final_unused_frame)) + "\n\n\n"

    print(log_str)

    if backup_flag == True:
        f = open(BACKUP_RECORD_FILE, 'a')
        f.write(log_str)
        f.close()


def removeAndBackupImage():
    getAllFileName()
    getAllCCBUsedFrame()
    checkUnusedFileInCCB()

    getAllSrcFile()
    checkUnusedFileInSrc()

########################

######################## remove sound

SOUND_JS = SRC_ROOT_PATH + "/global/sound.js"
FSM_JSON = RES_PATH + "/data/base_match_fsm.json"

SOUND_SEARCH_PATHS = [SOUND_JS, FSM_JSON]

all_sound_file = []

def getAllSoundFile():
    file_list = getAllExtFile(SOUNDS_ROOT_PATH, SOUNDS_EXT)
    all_sound_file.extend(file_list)

def removeSounds():
    #read file
    file_dic = {}
    for file in SOUND_SEARCH_PATHS:
        file_object = open(file)
        try:
            file_dic[file] = file_object.read()
        finally:
            file_object.close()

    log_str = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) + "\n"
    log_str += "---- start remove sounds...\n"
    count = 0
    for sound_file in all_sound_file:
        file_name = getFrameName(sound_file)
        if checkFrameInDic(file_name, file_dic) == False:
            count = count + 1
            log_str += sound_file.replace(PROJECT_PATH, "") + "\n"
            shutil.move(sound_file, BACKUP_SOUNDS_PATH + "/" + getFileName(sound_file))

    log_str += "---- end remove sound... remove count : " + str(count) + "\n\n\n"

    print(log_str)

    if backup_flag == True:
        f = open(BACKUP_RECORD_FILE, 'a')
        f.write(log_str)
        f.close()

def removeAndBackupSounds():
    getAllSoundFile()
    removeSounds()

#########################

if __name__ == "__main__":
    #getAllResourceFile()

    removeAndBackupImage()
    removeAndBackupSounds()