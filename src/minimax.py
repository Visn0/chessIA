
def evaluation(game):
    a = 1
    return a


def generate_moves(game):
    # TODO
    return []


def apply_move(new_game, move):
    # TODO
    a = 1
    return a


def better(new_score, best_score):
    # TODO depending if we want max or min score
    return new_score > best_score


def minimax(game, black_best, white_best, max_depth, depth,
            chosen_score, chosen_move, to_move_black):
    if depth == max_depth:
        chosen_score = evaluation(game)
    else:
        moves_list = generate_moves(game)

        if len(moves_list) == 0:
            chosen_score = evaluation(game)
        else:
            for the_move in moves_list:
                best_score = 999999
                new_game = game
                the_score = apply_move(new_game, the_move)
                minimax(new_game, black_best, white_best, max_depth, depth+1,
                        the_score, the_move, not to_move_black)

                if to_move_black:
                    if the_score > black_best:
                        if the_score > white_best:
                            break  # alpha_beta cutoff
                        else:
                            black_best = the_score

                else: #to_move_white
                    if the_score < white_best:
                        if the_score < black_best:
                            break  # alpha_beta cutoff
                        else:
                            white_best = the_score

                if better(the_score, best_score):
                    best_score = the_score
                    best_move = the_move

            chosen_score = best_score
            chosen_move = best_move


if __name__ == '__main__':
    print("Minimax class test")
