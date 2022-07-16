import array as arr

#inventory pathes
inv_pic=f'content\pictures\inventory\inventory.png'
inv_close=f'content\pictures\inventory\close.png'

#seed pathes
hole_pic=f'content\pictures\seeds\hole.png'
sfl_seed=f'content\pictures\seeds\sfl.png'
potato_seed=f'content\pictures\seeds\potato.png'
pumpkin_seed=f'content\pictures\seeds\pumpkin.png'
carrot_seed=f'content\pictures\seeds\carrot.png'
cabbage_seed=f'content\pictures\seeds\cabbage.png'
seed_pathes=[sfl_seed, potato_seed, pumpkin_seed,carrot_seed,cabbage_seed]

#plants pathes
sfl_pic=f'content\pictures\plants\sfl.png'
potato_pic=f'content\pictures\plants\potato.png'
pumpkin_pic=f'content\pictures\plants\pumpkin.png'
carrot_pic=f'content\pictures\plants\carrot.png'
cabbage_pic=f'content\pictures\plants\cabbage.png'
beetroor_pic=f'content\\pictures\\plants\\beetroot.png'

plants_pathes=[sfl_pic, potato_pic, pumpkin_pic, carrot_pic, cabbage_pic,beetroor_pic]

#other pathes
chest_pic=f'content\pictures\\troubles\chest.png'
close_text=f'content\pictures\\troubles\close.png'
ns_tl=f'content\pictures\\troubles\\no_seedtl.png'
ns_tr=f'content\pictures\\troubles\\no_seedtr.png'
ns_br=f'content\pictures\\troubles\\no_seedbr.png'
ns_bl=f'content\pictures\\troubles\\no_seedbl.png'
disconnect_pic=f'content\pictures\\troubles\\disconnect.png'
refresh_pic=f'content\pictures\\troubles\\refresh.png'
lets_farm_txt=f'content\pictures\\troubles\\lets_farm.png'


#goblin pathes
find_txt=f'content\pictures\\troubles\\find_goblin.png'
continue_txt=f'content\pictures\\troubles\\continue.png'
close_txt=f'content\pictures\\troubles\\close.png'
img_txt=f'content\\pictures\\troubles\\img_txt.png'
stealer=f'content\\pictures\\troubles\\stealer.png'

no_seed_pathes=list({ns_bl,ns_tl,ns_br,ns_tr})



for seed  in seed_pathes:
    print(seed)
