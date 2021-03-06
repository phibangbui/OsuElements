import shutil
from tempfile import mkstemp
from shutil import move
from os import remove, close, path
import os
import sys

# All the types of elements
class combobreak_sound:
	def __init__(self):
		self.breaksound = 'combobreak.wav'

class comboburst:
	def __init__(self):
		self.comboburst0 = 'comboburst-0.wav'
		self.comboburst1 = 'comboburst-1.wav'
		self.comboburst2 = 'comboburst-2.wav'
		self.comboburst3 = 'comboburst-3.wav'
		self.comboburst4 = 'comboburst-4.wav'
		self.comboburst5 = 'comboburst-5.wav'
		self.comboburst6 = 'comboburst-6.wav'
		self.comboburst7 = 'comboburst-7.wav'
		self.comboburst8 = 'comboburst-8.wav'

class comboburst_pic:
	def __init__(self):
		self.comboburst0 = 'comboburst-0.png'
		self.comboburst0HD = 'comboburst-0@2x.png'
		self.comboburst1 = 'comboburst-1.png'
		self.comboburst1HD = 'comboburst-1@2x.png'
		self.comboburst2 = 'comboburst-2.png'
		self.comboburst2HD = 'comboburst-2@2x.png'
		self.comboburst3 = 'comboburst-3.png'
		self.comboburst3HD = 'comboburst-3@2x.png'

class countdown:
	def __init__(self):
		self.one = 'count1s.wav'
		self.two = 'count2s.wav'
		self.three = 'count3s.wav'
		self.go = 'go.wav'
		self.goimg = 'go.png'
		self.ready = 'ready.wav'

class cursor:
	def __init__(self):
		self.cursor = 'cursor.png'
		self.cursortrail = 'cursortrail.png'
		self.star2 = 'star2.png'

class drum:
	def __init__(self):
		self.drumhit = 'drum-hitclap.wav'
		self.drumhitf = 'drum-hitfinish.wav'
		self.drumhitn = 'drum-hitnormal.wav'
		self.drumhitw = 'drum-hitwhistle.wav'
		self.sliders = 'drum-sliderslide.wav'
		self.sliderw = 'drum-sldierwhistle.wav'
		self.normalhc = 'normal-hitclap.wav'
		self.normalhc2 = 'normal-hitclap2.wav'
		self.normalhf = 'normal-hitfinish.wav'
		self.normalh = 'normal-hitnormal.wav'
		self.normalhw = 'normal-hitwhistle.wav'
		self.normalss = 'normal-sliderslide.wav'
		self.normalst = 'normal-slidertick.wav'
		self.normalw = 'normal-sliderwhistle.wav'
		self.normalw2 = 'normal-sliderwhistle2.wav'
		self.softhc = 'drum-sldierwhistle.wav'
		self.softhf= 'soft-hitclap.wav'
		self.softhn= 'soft-hitfinish.wav'
		self.softss= 'soft-sliderslide.wav'
		self.softst= 'soft-slidertick.wav'
		self.softsw= 'soft-sldierwhistle.wav'


class follow_point:
	def __init__(self):
		self.followpoint = 'followpoint.png'
		self.followpoint0 = 'followpoint-0.png'
		self.followpoint1 = 'followpoint-1.png'
		self.followpoint2 = 'followpoint-2.png'

class hit_score:
	def __init__(self):
		self.hitmiss = 'hit0.png'
		self.hit50 = 'hit50.png'
		self.hit50k = 'hit50k.png'
		self.hit100 = 'hit100.png'
		self.hit100k = 'hit100k.png'
		self.hit300 = 'hit300.png'
		self.hit300g = 'hit300g.png'
		self.hit300k = 'hit300k.png'

class hit_circle:
	def __init__(self):
		self.c0 = 'default-0.png'
		self.c1 = 'default-1.png'
		self.c2 = 'default-2.png'
		self.c3 = 'default-3.png'
		self.c4 = 'default-4.png'
		self.c5 = 'default-5.png'
		self.c6 = 'default-6.png'
		self.c7 = 'default-7.png'
		self.c8 = 'default-8.png'
		self.c9 = 'default-9.png'
		self.approachcircle = 'approachcircle.png'
		self.hitcircle = 'hitcircle.png'
		self.hitcircleoverlay = 'hitcircleoverlay.png'
		self.hitcircleselect = 'hitcircleselect.png'
		self.slider = 'sliderb0.png'
		self.sliderfollow = 'sliderfollowcircle.png'
		self.lighting = 'lighting.png'
		self.reversearrow = 'reversearrow.png'

class input_overlay:
	def __init__(self):
		self.inputbackground = 'inputoverlay-background.png'
		self.inputbackgroundHD = 'inputoverlay-background@2x.png'
		self.inputkey = 'inputoverlay-key.png'
		self.inputkeyHD = 'inputoverlay-key@2x.png'

class menu_click:
	def __init__(self):
		self.menuclick = 'menuclick.wav'

class spinner:
	def __init__(self):
		self.spinnerapproach = 'spinner-approachcircle.png'
		self.spinnerbackground = 'spinner-background.png'
		self.spinnerbonus = 'spinnerbonus.wav'
		self.spinnerbottom = 'spinner-bottom.png'
		self.spinnerclear = 'spinner-clear.png'
		self.spinnercircle = 'spinner-circle.png'
		self.spinnerglow = 'spinner-glow.png'
		self.spinnermetre = 'spinner-metre.png'
		self.spinnerosu = 'spinner-osu.png'
		self.spinnerrpm = 'spinner-rpm.png'
		self.spinnerspin = 'spinner-spin.png'
		self.spinnerspinsound = 'spinnerspin.wav'
		self.spinnertop = 'spinner-top.png'
		self.playwarning = 'play-warningarrow.png'

class section_fp:
	def __init__(self):
		self.passed = 'section-pass.png'
		self.failed = 'section-fail.png'
		self.passedsound = 'sectionpass.mp3'
		self.failedsound = 'sectionfail.mp3'

class fail_background:
	def __init__(self):
		self.failbackground = 'fail-background.png'

class pause_background:
	def __init__(self):
		self.pauseoverlay = 'pause-overlay.png'
		self.pauseback = 'pause-back.png'
		self.pausecontinue = 'pause-continue.png'
		self.pauseretry = 'pause-retry.png'

class rank_screen:
	def __init__(self):
		self.rankingA = 'ranking-A.png'
		self.rankingAHD = 'ranking-A@2x.png'
		self.rankingaccuracy = 'ranking-accuracy.png'
		self.rankingAs = 'ranking-A-small.png'
		self.rankingB = 'ranking-B.png'
		self.rankingBHD = 'ranking-B@2x.png'
		self.rankingback = 'ranking-back.png'
		self.rankingBs = 'ranking-B-small.png'
		self.rankingC = 'ranking-C.png'
		self.rankingCHD = 'ranking-C@2x.png'
		self.rankingCs = 'ranking-C-small.png'
		self.rankingD = 'ranking-D.png'
		self.rankingDHD = 'ranking-D@2x.png'
		self.rankingDs = 'ranking-D-small.png'
		self.rankinggraph = 'ranking-graph.png'
		self.rankingmax = 'ranking-maxcombo.png'
		self.rankingpanel = 'ranking-panel.png'
		self.rankingperfect = 'ranking-perfect.png'
		self.rankingreplay = 'ranking-replay.png'
		self.rankingretry = 'ranking-retry.png'
		self.rankingS = 'ranking-S.png'
		self.rankingSHD = 'ranking-S@2x.png'
		self.rankingSs = 'ranking-S-small.png'
		self.rankingSH = 'ranking-SH.png'
		self.rankingSHHD = 'ranking-SH@2x.png'
		self.rankingSHs = 'ranking-SH-small.png'
		self.rankingtitle = 'ranking-title.png'
		self.rankingX = 'ranking-X.png'
		self.rankingXHD = 'ranking-X@2x.png'
		self.rankingXH = 'ranking-XH.png'
		self.rankingXHHD = 'ranking-XH@2x.png'
		self.rankingXs = 'ranking-X-small.png'
		self.rankingXHs = 'ranking-XH-small.png'
		self.score0 = 'score-0.png'
		self.score1 = 'score-1.png'
		self.score2 = 'score-2.png'
		self.score3 = 'score-3.png'
		self.score4 = 'score-4.png'
		self.score5 = 'score-5.png'
		self.score6 = 'score-6.png'
		self.score7 = 'score-7.png'
		self.score8 = 'score-8.png'
		self.score9 = 'score-9.png'
		self.scorebg = 'scorebar-bg.png'
		self.scorecolour = 'scorebar-colour.png'
		self.scoreki = 'scorebar-ki.png'
		self.scorekidanger = 'scorebar-kidanger.png'
		self.scorekidnager2 = 'scorebar-kidanger2.png'
		self.scorecomma = 'score-comma.png'
		self.scoredot = 'score-dot.png'
		self.scorepercent = 'score-percent.png'
		self.scorex = 'score-x.png'

class ui:
	def __init__(self):
		self.buttonleft = 'button-left.png'
		self.buttonmiddle = 'button-middle.png'
		self.buttonright = 'button-right.png'
		self.stars = 'star.png'
		self.selectiontab = 'selection-tab.png'
		self.selectiontabHD = 'selection-tab@2x.png'
		self.menuback = 'menu-back.png'
		self.menubackHD = 'menu-back@2x.png'
		self.menubackground = 'menu-background.jpg'
		self.menubuttonbackground = 'menu-button-background.png'
		self.menubuttonbackgroundHD = 'menu-button-background@2x.png'
		self.selectionauto = 'selection-mod-autoplay.png'
		self.selectionautoHD = 'selection-mod-autoplay@2x.png'
		self.selectioncinema = 'selection-mod-cinema.png'
		self.selectioncinemaHD = 'selection-mod-cinema@2x.png'
		self.selectiondt = 'selection-mod-doubletime.png'
		self.selectiondtHD = 'selection-mod-doubletime@2x.png'
		self.selectioneasy = 'selection-mod-easy.png'
		self.selectioneasyHD = 'selection-mod-easy@2x.png'
		self.selectionfadein = 'selection-mod-fadein.png'
		self.selectionfadeinHD = 'selection-mod-fadein@2x.png'
		self.selectionfl = 'selection-mod-flashlight.png'
		self.selectionflHD = 'selection-mod-flashlight@2x.png'
		self.selectionht = 'selection-mod-halftime.png'
		self.selectionhtHD = 'selection-mod-halftime@2x.png'
		self.selectionhr = 'selection-mod-hardrock.png'
		self.selectionhrHD = 'selection-mod-hardrock@2x.png'
		self.selectionhd = 'selection-mod-hidden.png'
		self.selectionhdHD = 'selection-mod-hidden@2x.png'
		self.selection4k = 'selection-mod-key4.png'
		self.selection4kHD = 'selection-mod-key4@2x.png'
		self.selection5k = 'selection-mod-key5.png'
		self.selection5kHD = 'selection-mod-key5@2x.png'
		self.selection6k =  'selection-mod-key6.png'
		self.selection6kHD =  'selection-mod-key6@2x.png'
		self.selection7k = 'selection-mod-key7.png'
		self.selection7kHD = 'selection-mod-key7@2x.png'
		self.selection8k = 'selection-mod-key8.png'
		self.selection8kHD = 'selection-mod-key8@2x.png'
		self.selectionnc = 'selection-mod-nightcore.png'
		self.selectionncHD = 'selection-mod-nightcore@2x.png'
		self.selectionnf = 'selection-mod-nofail.png'
		self.selectionnfHD = 'selection-mod-nofail@2x.png'
		self.selectionpf = 'selection-mod-perfect.png'
		self.selectionpfHD = 'selection-mod-perfect@2x.png'
		self.selectionrd = 'selection-mod-random.png'
		self.selectionrdHD = 'selection-mod-random@2x.png'
		self.selectionrx = 'selection-mod-relax.png'
		self.selectionrxHD = 'selection-mod-relax@2x.png'
		self.selectionap = 'selection-mod-relax2.png'
		self.selectionapHD = 'selection-mod-relax2@2x.png'
		self.selectionso = 'selection-mod-spunout.png'
		self.selectionsoHD = 'selection-mod-spunout@2x.png'
		self.selectionsd = 'selection-mod-suddendeath.png'
		self.selectionsdHD = 'selection-mod-suddendeath@2x.png'
		self.selectiontg = 'selection-mod-target.png'
		self.selectiontgHD = 'selection-mod-target@2x.png'

options = {combobreak_sound : combobreak_sound(),
			comboburst : comboburst(),
			comboburst_pic : comboburst_pic(),
			countdown : countdown(),
			cursor : cursor(),
			drum : drum(),
			follow_point : follow_point(),
			hit_score : hit_score(),
			hit_circle : hit_circle(),
			input_overlay : input_overlay(),
			menu_click : menu_click(),
			spinner : spinner(),
			section_fp : section_fp(),
			fail_background : fail_background(),
			pause_background : pause_background(),
			rank_screen : rank_screen(),
			ui : ui()
			}

# src : folder of skin we want to copy from
# dst : folder of skin we want to copy to
# element_name : class name of what we want to copy, must be one of the keys in options
def transfer_files(src, dst, element_name):
	element_class = options[element_name]
	# iterate through all of the class 'files' 
	for attr, value in element_class.__dict__.iteritems():
		# check if src folder contains all files, if not then delete the files that the src does not contain in the dst folder
		# in the case that src doesnt have HD element but dst does
		if(not os.path.isfile(src + "/" + value)):
			if(not os.path.isfile(dst + "/" + value)):
				continue
			else:
				os.remove(dst + "/" + value)
		else: 
			shutil.copyfile(src + "/" + value, dst + "/" + value)

# create an entirely new skin to copy elements to, copies a base skin first
# rewrites the skin.ini to change the name/version/author
# should always be called so that skins don't get overwritten
def safe_copy(src, dst, skinname):
	shutil.copytree(src, dst)
	#Create temp file
	fh, abs_path = mkstemp()
	new_file = open(dst + "/skin.ini",'w')
	old_file = open(src + "/skin.ini")
	for line in old_file:
		if 'Name: ' in line:
			new_file.write('Name: ' + skinname + '\n')
		elif 'Version: ' in line:
			new_file.write('Version: 1\n')
		elif 'Author: ' in line:
			new_file.write('Author: OsuElements\n')
		else:
			new_file.write(line)
	new_file.close()
	close(fh)
	old_file.close()

def start_point():
	selection1 = raw_input("[1] : Create a new skin from a base skin \n" +
				"[2] : Copy elements from an existing skin to another existing skin (WARNING, elements will be overwritten and lost!)\n ")
	menuchoice1 = {'1' : select_1, '2' : select_2}
	menuchoice1[selection1]()

def select_1():
	print ('Creating a new skin from a base skin selected\n')
	skinlist = [f for f in os.listdir('.') if not os.path.isfile(f)]
	select_1_skinchoice = {}
	skin_list = ""
	for i, skin in enumerate(skinlist):
		skin_list += '[' + str(i + 1) + '] : ' + skin + ' \n'
		select_1_skinchoice[str(i + 1)] = skin	
	src = raw_input('Please enter the  foldername of the skin you want to rip: \n' +
			skin_list)
	dst = raw_input('Please enter the foldername of the new skin to live in: ')
	skinname = raw_input('Please give the new skin a name!: ')
	safe_copy(select_1_skinchoice[src], dst, skinname)
	post_copy_select = raw_input("annnnnd it's done, what would you like to do now\n"
		"[1] Let me start copying elements from other skins into my newly made skin\n"
		"[2] Bring me back to the start menu\n"
		"[3] Exit\n")
	if (post_copy_select == '1'):
		select_2()
	elif (post_copy_select == '2'):
		start_point()
	elif (post_copy_select == '3'):
		sys.exit()
	else:
		print 'bro you didnt even enter anything valid... bringing you back to the home screen\n'
		start_point()
		
def select_2():
	print ('Copying elements from an existing skin to another skin selected\n')
	skinlist = [f for f in os.listdir('.') if not os.path.isfile(f)]
	select_2_skinchoice = {}
	skin_list = ""
	for i, skin in enumerate(skinlist):
		skin_list += '[' + str(i + 1) + '] : ' + skin + ' \n'
		select_2_skinchoice[str(i + 1)] = skin	
	src = raw_input('Please enter the foldername of the skin you want to rip from: \n' +
			skin_list)
	dst = raw_input('Please enter the foldername of the skin you want to replace elements to: \n' +
			skin_list)
	select_2_elementselect(select_2_skinchoice[src], select_2_skinchoice[dst])
	
def select_2_elementselect(src, dst):
	element_name = raw_input('Select from one of the following element_types: \n' +
				'[1] : Combobreak Sound \n' +
				'[2] : Comboburst\n' +
				'[3] : Comboburst Picture\n' +
				'[4] : Countdown\n' +
				'[5] : Cursor\n' +
				'[6] : Hit Sound\n' +
				'[7] : Follow Points\n' +
				'[8] : Hit Score\n' +
				'[9] : Hit Circles\n' +
				'[10] : Input Overlay (The Z, X, Mouse1, Mouse2 counters)\n' +
				'[11] : Menu Click Sounds\n' +
				'[12] : Spinner\n' +
				'[13] : Section Fail and Passes (Both sound and picture)\n' +
				'[14] : Song Fail Background\n' +
				'[15] : Song Pause Background\n' +
				'[16] : Rank Screen\n' +
				'[17] : General UI (Song select, Background, etc...)\n')

	menuchoice2 = {'1' : combobreak_sound, '2' : comboburst, '3' : comboburst_pic, '4' : countdown, '5' : cursor, '6' : drum, '7' : follow_point,
		'8' : hit_score, '9' : hit_circle, '10' : input_overlay, '11' : menu_click, '12' : spinner, '13' : section_fp, '14' : fail_background,
		'15' : pause_background, '16' : rank_screen, '17' : ui
		}
	element_type = menuchoice2[element_name]
	confirm_element(src, dst, element_type)

def confirm_element(src, dst, element_type):
	confirm = raw_input('Are you sure you want to copy this element?\n' +
			'[1] Yes, copy it!\n' +
			'[2] No, Bring me back to the element select screen\n'
			'[3] Preview Element\n')
	if (confirm == '1'):
		transfer_files(src, dst, element_type)
		go_again = raw_input('Copied! would you like to copy more elements from this skin?\n' +
			     '[1] Yes, give me the element choice selection screen again\n' +
			     '[2] No, but i would like to rip elements from another skin\n' +
			     '[3] No, and i would like to quit the program\n')
		if (go_again == '1'):
			select_2_elementselect(src, dst)
		elif (go_again == '2'):
			select_2()
		elif (go_again == '3'):
			sys.exit()
		else:
			print 'bro you didnt even enter anything valid... bringing you back to the select screen\n'
			select_2()
	elif (confirm == '2'):
		select_2_elementselect(src, dst)
	elif (confirm == '3'):
		return	

print ('Hello! Welcome to OsuElements Python Script! \n' +
	"Because I didn't feel like creating a gui for this script, \n" +
	"You can just follow the following requests in the command prompt to rip your skins! \n"
	"- phibangbui.cs@gmail.com for any questions about the script \n")
start_point()

