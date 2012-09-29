hgdm_par = {
'tie_slm_tie_slm_tie_slm':
    [{}, # -- layer 0 has no filter
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'}],
'tie_slm_tie_slm_tie_pca':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'pca',
      'f_key': 'tie_pca'}],
'tie_slm_tie_slm_tie_pls':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'pls',
      'f_key': 'tie_pls'}],
'tie_slm_tie_slm_til_pca':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tiled',
      'f_learn_algo': 'pca',
      'f_key': 'til_pca'}],
'tie_slm_tie_slm_til_pls':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tiled',
      'f_learn_algo': 'pls',
      'f_key': 'til_pls'}],
'til_slm_til_slm_til_slm':
    [{},
     {'architecture': 'tiled',
      'f_learn_algo': 'slm',
      'f_key': 'til_slm'},
     {'architecture': 'tiled',
      'f_learn_algo': 'slm',
      'f_key': 'til_slm'},
     {'architecture': 'tiled',
      'f_learn_algo': 'slm',
      'f_key': 'til_slm'}],
'tie_slm_tie_pca_til_pls':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tied',
      'f_learn_algo': 'pca',
      'f_key': 'tie_pca'},
     {'architecture': 'tiled',
      'f_learn_algo': 'pls',
      'f_key': 'til_pls'}],
'tie_slm_til_pca_til_pls':
    [{},
     {'architecture': 'tied',
      'f_learn_algo': 'slm',
      'f_key': 'tie_slm'},
     {'architecture': 'tiled',
      'f_learn_algo': 'pca',
      'f_key': 'til_pca'},
     {'architecture': 'tiled',
      'f_learn_algo': 'pls',
      'f_key': 'til_pls'}],
}