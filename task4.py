good = r"""
      _\       
       /`b  
  /####J   
   |\ ||   Asik
"""
bad = r"""
            _.===._      ,"^^^^",
           /_\^^^/_\    /  ^ ,^  \     ,
           (0\ ^ /0)\  / ^  /  ^  \    /\
            \     /  ^^   ^ \ ^ \  ",." /
             )   (  ^  ^   ^ \   \    ,'
             (o_o)^    \ ^   ,)  /`^^`
              ^V^\ ^ \  \_,-"((((
      jgs     /  /`""/  /
             (((`   '(((
"""
drawbridge_raised = False
if not drawbridge_raised:
    outcome = "Thunder: We need to cross the bridge. "
    print(good)
else:
    outcome = "Doom: We're going to die in here."
    print(bad)
