class Move_Checks:

  def __init__(self, game_state):
    self.game_state = game_state
    self.my_body = self.game_state['you']['body']
    self.my_head = self.game_state["you"]["body"][0]
    self.board_width = self.game_state['board']['width']
    self.board_height = self.game_state['board']['height']
    self.head_left = {'x' : self.my_head["x"] - 1, 'y' : self.my_head["y"]}
    self.head_right = {'x' : self.my_head["x"] + 1, 'y' : self.my_head['y']}
    self.head_down = {'x' : self.my_head["x"], 'y' : self.my_head["y"] - 1}
    self.head_up = {'x' : self.my_head["x"], 'y' : self.my_head['y'] + 1}
    self.opponents = self.game_state['board']['snakes']
    

  def self_collision_prevention(self, is_move_safe):
    # if own body is infront find a way that is not a trap
    # print(f'my body {self.my_body}')
    if self.head_left in self.my_body:
      is_move_safe["left"] = False

    if self.head_right in self.my_body:
      is_move_safe["right"] = False

    if self.head_down in self.my_body:
      is_move_safe["down"] = False

    if self.head_up in self.my_body:
      is_move_safe["up"] = False
    
    return is_move_safe

  def stay_on_board(self, is_move_safe):
    if self.head_left['x'] < 0:
      is_move_safe["left"] = False

    if self.head_right['x'] > (self.board_width - 1):
      is_move_safe["right"] = False

    if self.head_down['y'] < 0:
      is_move_safe["down"] = False

    if self.head_up['y'] > (self.board_height - 1):
      is_move_safe["up"] = False

    return is_move_safe

  def eek_other_snakes(self, is_move_safe):
    # opponents [{'id': 'gs_bp7ddpFc47WbMtYpMcjdSqtJ', 'name': 'Pythoninator', 'latency': '148', 'health': 97, 'body': [{'x': 10, 'y': 3}, {'x': 10, 'y': 2}, {'x': 10, 'y': 1}, {'x': 9, 'y': 1}, {'x': 9, 'y': 2}, {'x': 9, 'y': 3}, {'x': 9, 'y': 4}, {'x': 10, 'y': 4}, {'x': 10, 'y': 5}, {'x': 10, 'y': 6}, {'x': 9, 'y': 6}, {'x': 8, 'y': 6}, {'x': 7, 'y': 6}, {'x': 7, 'y': 7}, {'x': 8, 'y': 7}, {'x': 9, 'y': 7}, {'x': 10, 'y': 7}], 'head': {'x': 10, 'y': 3}, 'length': 17, 'shout': '', 'squad': '', 'customizations': {'color': '#ff66a3', 'head': 'beluga', 'tail': 'curled'}}]
    # remove self from opponents
    # combine head and body
    # if close and health is less than mine, attack
    if self.game_state['you'] in self.opponents:
      self.opponents.remove(self.game_state['you'])

    opponents_positions = {k:v for (k, v) in self.opponents}
    print(opponents_positions)
    return is_move_safe

  def build_opponent_snake(snake_parts):
    print(snake_parts)
    snake = snake_parts['body']
    snake.append((snake_parts['head']))
    return snake

  def check_moves(self, is_move_safe):
    is_move_safe = self.self_collision_prevention(is_move_safe)
    is_move_safe = self.stay_on_board(is_move_safe)
    is_move_safe = self.eek_other_snakes(is_move_safe)
    return is_move_safe