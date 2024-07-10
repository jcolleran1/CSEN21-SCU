class Agent:
    #checks if both locations are clean
    def goal_test(self, state):
        if state[0] == "Clean" and state[1] == "Clean":
            return True
        else:
            return False

    #Determines the possible actions given a current state
    #Takes current state as input and returns possible actions
    def actions(self, state):
        possible_actions = []
        #if the state is dirty suck is a possible function
        if state[state[2]] == "Dirty":
            possible_actions.append("Suck")
        #if state is on the right go left is an action
        elif state[2] == 1:  
            possible_actions.append("Left")
            #if state is on the left go right is an action
        else:
            possible_actions.append("Right")
        return possible_actions

    #updates the state based on the current action 
    #takes the current state and action as an input and returns the new state after the action
    def update(self, state, action):
        #makes a copy of the current state
        new_state = state.copy()
        #if action is suck then the new state is clean
        if action == "Suck":
            new_state[new_state[2]] = "Clean"
        #updates states location
        elif action == "Left":
            new_state[2] = 0
        elif action == "Right":
            new_state[2] = 1 
        return new_state

    #excutes the action of the agent until goal state
    def run(self, initial_state):
        state = initial_state
        action_seq = []
        total_cost = 0
        #It repeatedly selects actions, updates the state, and 
        #increments the total cost until the goal state is reached.
        while not self.goal_test(state):
            possible_actions = self.actions(state)
            action = possible_actions[0]
            action_seq.append(action)
            total_cost += 1
            state = self.update(state, action)
        #returns the actions and total cose
        return action_seq, total_cost


# Test case
def test_vacuum_cleaner_agent():
    test_cases = [
        (["Dirty", "Dirty", 0], ["Suck", "Right", "Suck"], 3),
        (["Clean", "Dirty", 0], ["Right", "Suck"], 2),
        (["Dirty", "Clean", 1], ["Left", "Suck"], 2),
        (["Clean", "Clean", 0], [], 0),
        (["Dirty", "Dirty", 1], ["Suck", "Left", "Suck"], 3),
        (["Clean", "Dirty", 1], ["Suck"], 1),
        (["Dirty", "Clean", 0], ["Suck"], 1),
        (["Clean", "Clean", 1], [], 0),
    ]

    for initial_state, expected_actions, expected_cost in test_cases:
        agent = Agent()
        actions_taken, total_cost = agent.run(initial_state)
        if actions_taken == expected_actions and total_cost == expected_cost:
            print("Correct Outputs!")
        else:
            print("Wrong Outputs!")

test_vacuum_cleaner_agent()
