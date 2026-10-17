class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):
        if not occupied:
            target_mode = "ECO"
        elif temp > 26:
            target_mode = "COOL"
        elif temp < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"
        if target_mode == self.previous_mode:
            command_sent = False
        else:
            command_sent = True   
            self.previous_mode = target_mode
        return target_mode, command_sent
agent = StatefulClassroomAgent()
percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]

print("Step | Percept (Temp, Occupied) | Target Mode | Command Sent?")
print("-" * 55)
for step, percept in enumerate(percepts, 1):
    target, sent = agent.act(*percept)
    print(f"{step:4} | {str(percept):24} | {target:11} | {str(sent)}")