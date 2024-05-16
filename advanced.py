'''Python: Advanced

70 points

This assignment will develop your ability to manipulate data.
We expect that this assignment will equip you to understand
    Python tutorials.

Please refer to the file `advanced_sample_data.py` for examples of:
- the `social_graph` parameter for the relationship_status item
- the `board` parameter for the tic_tac_toe item
- the `route_map` parameter for the eta item
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see `advanced_sample_data.py` for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if from_member follows to_member,
        "followed by" if from_member is followed by to_member,
        "friends" if from_member and to_member follow each other,
        "no relationship" if neither from_member nor to_member follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    relationship = "no relationship"
    follower = False
    followed_by = False

    for user_name in social_graph:
        if user_name == from_member:
            followers_list = social_graph[user_name]["following"]
            if followers_list.count(to_member) > 0:
                follower = True

        if user_name == to_member:
            followers_list = social_graph[user_name]["following"]
            if followers_list.count(from_member) > 0:
                followed_by = True

    if follower:
        if followed_by:
            relationship = "friends"
        else:
            relationship = "follower"
    else:
        if followed_by:
            relationship = "followed by"

    return relationship


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see `advanced_sample_data.py` for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner, or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    winner_symbol = "NO WINNER"
    winner_exist = False
    
    row_size = len(board[0])

    # check horizontal
    i = 0
    while i < row_size:
        chk_symbol = board[i][0]
        winner_row = True

        j = 1
        while j < row_size:
            if chk_symbol != board[i][j]:
                winner_row = False
                break
            j = j + 1

        if winner_row:
            winner_symbol = chk_symbol
            winner_exist = True
            break
        i = i + 1

    # check vertical
    if not winner_exist:
        i = 0
        while i < row_size:
            chk_symbol = board[0][i]
            winner_col = True

            j = 1
            while j < row_size:
                if chk_symbol != board[j][i]:
                    winner_col = False
                    break
                j = j + 1

            if winner_col:
                winner_symbol = chk_symbol
                winner_exist = True
                break
            i = i + 1
        
        # check diagonal from upper left to lower right
        if not winner_exist:
            chk_symbol = board[0][0]
            winner_diag = True

            i = 1
            j = 1
            while i < row_size:
                if chk_symbol != board[i][j]:
                    winner_diag = False
                    break
                i = i + 1
                j = j + 1

            if winner_diag:
                winner_symbol = chk_symbol
                winner_exist = True

        # check diagonal from lower left to upper right
        if not winner_exist:
            i = row_size - 1
            j = 0
            chk_symbol = board[i][j]
            winner_diag = True

            i = i - 1
            j = j + 1
            while j < row_size:                
                if chk_symbol != board[i][j]:
                    winner_diag = False
                    break
                i = i - 1
                j = j + 1

            if winner_diag:
                winner_symbol = chk_symbol
                winner_exist = True
                
    return winner_symbol 

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see `advanced_sample_data.py` for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    travel_time = 0
    from_leg = first_stop

    for route_rec in route_map:
        if from_leg == route_rec[0]:
            travel_time = travel_time + route_map[route_rec] ["travel_time_mins"]
            from_leg = route_rec[1]
        if second_stop == route_rec[1]:
            break

    return travel_time
