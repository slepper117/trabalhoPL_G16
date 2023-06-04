
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-left*ASSIGN ESCREVER NUMBER VARIDexpression : expression '+' expression\n                      | expression '-' expression\n                      | expression '*' expressionexpression : NUMBERexpression : VARID"
    
_lr_action_items = {'NUMBER':([0,4,5,6,],[2,2,2,2,]),'VARID':([0,4,5,6,],[3,3,3,3,]),'$end':([1,2,3,7,8,9,],[0,-4,-5,-1,-2,-3,]),'+':([1,2,3,7,8,9,],[4,-4,-5,-1,-2,-3,]),'-':([1,2,3,7,8,9,],[5,-4,-5,-1,-2,-3,]),'*':([1,2,3,7,8,9,],[6,-4,-5,6,6,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,4,5,6,],[1,7,8,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression + expression','expression',3,'p_expression','arith_grammar.py',24),
  ('expression -> expression - expression','expression',3,'p_expression','arith_grammar.py',25),
  ('expression -> expression * expression','expression',3,'p_expression','arith_grammar.py',26),
  ('expression -> NUMBER','expression',1,'p_expression_number','arith_grammar.py',30),
  ('expression -> VARID','expression',1,'p_expression_varid','arith_grammar.py',34),
]