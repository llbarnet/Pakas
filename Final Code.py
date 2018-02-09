#### All Nap Code##############
def nap_activity():
  wake_up_answer = str(raw_input('Yes or No'))
  if wake_up_answer.lower() == 'yes':
    print "Smart decision, how will you wake %s up?" %name
    def wake_up_method():
      coma_list = ['no_coma', 'coma']
      coma_result = coma_list[randint(0,1)]
      method_choice = str(raw_input('Shake or Yell?'))
      name_length = len(name)
      ###here is print code to remove
      ##print coma_result
      ##print name_length
      ## shake choice
      if method_choice.lower() == 'shake':
        def shake_amt():
          print "how many shakes?"
          shakes_chosen = (raw_input('enter a number of shakes'))
          if shakes_chosen.isnumeric() == False:
            print "You can't shake %s like that..." %name
            return shake_amt()
          if (int(shakes_chosen) * name_length)%2  == 0 and coma_result == 'coma':
            print "You shook %s way too much! They were a delicate flower and your shaking has killed them!" %name
            print '%s will be sorely missed' %name
            print 'Game Over :((('
          if (int(shakes_chosen) * name_length)%2  != 0 and coma_result == 'coma':
            print "You shook %s way too much! They were a delicate flower and your shaking has killed them!" %name
            print '%s will be sorely missed' %name
            print 'Game Over :((('
          if (int(shakes_chosen) * name_length)%2  == 0 and coma_result == 'no_coma':
            print "There we are, %s is awake and ready to go" %name
            print "Are you ready to continue the adventure?"
            return cont_from_activity()
          if (int(shakes_chosen) * name_length)%2  != 0 and coma_result == 'no_coma':
            print "There we are, %s is awake and ready to go" %name
            print "Are you ready to continue the adventure?"
            return cont_from_activity() 
        return shake_amt()    
        
        
        
      ##Yell choice  
      if method_choice.lower() == 'yell':
        print "OK! Type some A's and H's to wake up %s" %name
        def yell_function():
          yell = str(raw_input("Yell some A's and H's"))
          yell_a_count = yell.lower().count('a')
          yell_h_count = yell.lower().count('h')
          ###here is print code to remove###
          ##print yell_a_count
          ##print yell_h_count
          yell_total_count = yell_a_count + yell_h_count
          if yell_total_count == 0:
            print "that was pretty weak, no A's or H's"
            print "try again"
            return yell_function() 
          if (yell_total_count * name_length)%2  == 0:
            print "Thats weird, %s wouldn't wake up! Even with all that yelling!" %name
            print "It looks like %s has fallen in a coma! And who knows when they will wake up" %name
            print "Seems like %s's adventure time is over, for now..." %name
            print "Game Over :((("
          if (yell_total_count * name_length)%2  != 0:
            print "sheesh!! You didn't have to yell that much, %s is up!"
            print "continue the adventure?"
            return cont_from_activity
        return yell_function() 
        
        
        
      else:
        print "%s will only wake up with a shake or a yell, try again" %name
        return wake_up_method()
      
    return wake_up_method()  
    end  
  if wake_up_answer.lower() == 'no':
    print 'I guess %s could use some more sleep' %name
    print 'wake %s up now?' %name
    return nap_activity()
  else:
    print 'a simple Yes or No will suffice'
    return nap_activity()






#### All Chess activity code############
def choke_resolve():
  choke_choice = str(raw_input('Yes or No'))
  choke_save_list = ['save', 'no_save']
  choke_save = choke_save_list[randint(0,1)]
  if choke_choice.lower() == 'yes' and choke_save == 'save':
    print "Great Work! Good thing you took that first aid class! %s is roughed up but they're safe!" %name
    print "Continue the Adventure?"
    return cont_from_activity()
  if choke_choice.lower() == 'yes' and choke_save == 'no_save':  
    print "What the Heck! You didn't know the Heimlich! You confused what you knew and gave %s CPR?!" %name
    print "Sadly %s didn't make it, %s will be missed" %name
    print 'Game Over :((('
    raw_input()
    end
  if choke_choice.lower() == 'no':
    print 'How Heartless! Well we say a heartfelt goodbye to %s' %name
  else:
    print 'lets start with a yes or no'
    return choke_resolve()

def chess_activity():
  first_mover = str(raw_input("you or %s"%name))
  paka = name
  choke = ['no', 'yes']
  choke_outcome = choke[randint(0,1)]
  ###here is print code to remove
  ##print choke_outcome
  if first_mover.lower() == 'you' or  first_mover == 'me' and choke_outcome == 'no':
    print 'Nice move! Unfortunately, %s beat you in the end, they are pretty good at chess afterall.' %name
    print 'Would you like the adventure to continue?'
    return cont_from_activity()
  
  if first_mover.lower() == 'you' or first_mover == 'me' and choke_outcome == 'yes':
    print 'Holey Moley! while you were thinking about your move, %s ate a chess piece and now they are choking!' %name
    print "You're pretty sure you know the Heimlich! Administer it?!"
    return choke_resolve()
  
  if first_mover.lower() == paka and choke_outcome == 'no':
    print "Well %s isn't the best at chess but you didn't have to beat them that bad" %name
    print 'Would you like the adventure to continue?'
    return cont_from_activity()
  
  if first_mover.lower() == paka and choke_outcome == 'yes':
    print "Instead of moving a chess piece you're silly %s decided to try and eat it, now they're choking!!" %name
    print "You're pretty sure you know the Heimlich! Administer it?!"
    return choke_resolve()
  
  else:
     print "They can't play chess, pick someone playing!"
     return chess_activity()
  

##### All Jump Rope Code######################
def jump_rope_activity():
  jump_amt = (raw_input('enter a number!'))
  if jump_amt.isnumeric() == False: 
    print 'just a number there bub'
    return jump_rope_activity()
  if (int(jump_amt) * 7)%2  == 0:
    print "fun! %s got some fun jumping in!" %name
    print "Do you want to continue the adventure?"
    return cont_from_activity()
  if (int(jump_amt) * 7)%2  != 0:
    print "ahhh! %s jumped too much and now has gotten tangled in the rope and is strangling!"%name
    print "quick! use your knife to cut %s out of this ropey hell!" %name
    def knife_cut():
      raw_input('Hit Enter to Draw Knife!')
      knife_good = ['knife', 'spoon']
      correct_knife = knife_good[randint(0,1)]
      ###Here is print code to remove
      ##print correct_knife
      if correct_knife == 'knife':
        print "Nice work! you cut %s out and %s wiggled out of the tangled death trap!" %(name, name)
        print "Do you want to continue the adventure?"
        return cont_from_activity()
      if correct_knife == 'spoon':  
        print "Son of a Gun! You brought a Spoon not a Knife! %s struggles but its no use." %name
        print "%s will be sorely missed" %name
        print 'Game Over :((('
    return knife_cut()      
###All Fetch Activity code######################
def throw_again():
  thrw_again_answ = str(raw_input('yes or no'))
  if thrw_again_answ.lower() == 'yes':
    return fetch_activity()
    end
  if thrw_again_answ == 'no':
    print 'No worries, do you want to keep the adventure alive?'
    return cont_from_activity()
    end
  else:
    print "just a yes or no"
    return throw_again()
def fetch_activity():
  throw_hand = ['left', 'right']
  deadly_throw = throw_hand[randint(0,1)]
  ###here is print code to remove
  ##print deadly_throw
  throw = str(raw_input('Left or Right'))
  if throw == deadly_throw:
    print "Whoops! you threw it too far and %s chased it off a cliff!" %name
    print "BUT! you remember %s was wearing a parachute! Quick! will you pull %s's chute!?" %(name, name)
    def chute_choice():
      chutes = ['open', 'close']
      chute_result = chutes[randint(0,1)]
      ##Here is print code to remove
      ##print chute_result
      cht_choice = str(raw_input('Yes or No'))
      if cht_choice.lower() == 'yes' and chute_result == 'open':
        print "congrats the chute opened and %s is safely floating to the ground" %name
        print "Do you wish to continue the adventure?"
        return cont_from_activity()
      if cht_choice.lower() == 'yes' and chute_result == 'close':
        print """Nooooo, you opened the chute but as the cloth unfurled moths and shreds of 
the parachute erupt into the sky, you watch as %s tumbles to doom""" %name
      end
      if cht_choice.lower() == 'no':
        print 'well thats cool, bye bye %s, SPLAT' %name
      else:
        print "not a choice"
        return chute_choice()
    return chute_choice()    
    end 
  if throw.lower() != deadly_throw and throw.lower() in throw_hand:
    print 'Nice throw! %s enjoyed that! Throw it again?' %name
    return throw_again()  
    
    
  else:
    print "only left or right hand bud"
    return fetch_activity()
      
      
##code to choose activity###################################      
def play_activity():
  game = str(raw_input('Fetch, Jump Rope, or Chess?'))
  if game.lower() == 'fetch':
    print 'Great Choice!'
    print '%s is so excited to play Fetch!' %name
    print 'Go ahead, Throw the Ball!, Will you use your left or right hand?'
    return fetch_activity()
  if game.lower() == 'jump rope':
    print 'Great Choice!'
    print 'how many jumps will %s jump?!' %name
    return jump_rope_activity()
  if game.lower() == 'chess':
    print 'Great Choice'
    print 'Who will make the first move, you or %s' %name
    return chess_activity()
  else:
    print 'try again'
    return play_activity()
    
    
##Starting game over from activity success######################################
def cont_from_activity():
  cont_choice = str(raw_input('Yes or No?'))
  if cont_choice.lower() == 'yes':
    print 'Awesome, let the game continue!'
    return activity()
  if cont_choice.lower() == 'no':
    print "I mean, if that's what you really want...goodbye"
  else:
    print 'Pardon?'
    return cont_from_activity()

##Feed activity################################################
def feed_activity():
      list_food = ['potato', 'cereal', 'toast', 'meatball', 'special treat']
      poison_food = list_food[randint(0,4)]
      ###here is print code to remove
      ##print poison_food
      print 'Ok! What shall %s eat?' %name
      food = str(raw_input('Potato, Cereal, Toast, Meatballs, or Special Treat?'))
      if food.lower() == poison_food:
        print 'OH NO!The %s was poisonous to %s!' %(poison_food, name)
        print """%s will die if you don't do something! 
You can save %s if you give it one of your handy antidotes!""" %(name, name)
        print 'Will you give %s the antidote?!' %name
        
        def give_antidote():
          decision_antid = str(raw_input('Yes or No'))
          antidote_list = ['purple', 'green']
          correct_anti = antidote_list[randint(0,1)]
          ###here is print code to remove
          ##print correct_anti
          if decision_antid.lower() == 'yes':
            print """Shoot! the labels of your antidotes fell off, 
and now you're not sure which antidote will cure your %s!""" %name
            print "You have an important decision to make, the green or purple antidote?"
            def antidote_run():
              anti_color_choice = str(raw_input('Green or Purple'))
              if anti_color_choice.lower() == correct_anti:
                print "You did it!!! You saved %s" %name
                print "It was a close call but your Paka lives to see another day! Do you wish to continue the adventure?"
                return cont_from_activity()
                end
              if anti_color_choice.lower() != correct_anti and anti_color_choice.lower() in antidote_list:
                print """Nooooooooo, you've chosen the wrong antidote! %s crumbles to the floor.
                %s will be sorely missed""" %(name, name)
                print "GAME OVER :("
                raw_input()
                end
              else:
                print "That's not even on the table! Do you want %s to die?! Try again" %(name)
                return antidote_run()
            return antidote_run()
            antidote_run()
          if decision_antid.lower() == 'no':
            print "Wow...well, your paka had a good run. RIP %s" %name
            print "Game Over :(("
            raw_input()
          else:
            print "whoops, just a yes or no question there"
            return give_antidote()
          end
        give_antidote() 
        end    
      if food.lower() != poison_food and food.lower() in list_food:
        print 'Yumm, %s liked that' %name
        print 'Now that %s has eaten what will you do with %s next?' %(name, name)
        return activity()
      
      else:
        print "hmm that isn't somehting %s can eat, Try again" %name
        return feed_activity()

##Beginning code to start game##
from random import randint
print """Hello and Welcome to the world of Pakas! 
Pakas live in a dangerous world full of poisonous foods, dangerous activities, and other life threatening obstacles!
Try your best to keep your Paka alive"""
print """INSTRUCTIONS: 
When prompted. write in your choice and press enter!
              GOOD LUCK!"""
print 'First you must Name your Paka!'
name = str(raw_input('Name:'))
print 'Wow! %s is such a good name!' %name
print 'You can now choose what to do with %s' %name
print 'Will you Feed it? Play with it? Or Put it in a Nap?'
def activity():
  act = str(raw_input('Feed, Play, Nap?'))
  if act.lower() == 'feed':
    return feed_activity()
    
  if act.lower() == 'play':
    print 'What game shall we play?'
    return play_activity()
    
  if act.lower() == 'nap':
    print 'ZZZZZZZ'
    print 'Time to wake up %s?' %name 
    return nap_activity()
    
  else:
    print "You can't do that with %s! Try again" %name
    return activity()
activity()

