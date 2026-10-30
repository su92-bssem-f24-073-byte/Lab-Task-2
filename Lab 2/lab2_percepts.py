class ClassroomAgent:
    def __init__(self):
        self.previous_mode = None
    def evaluate_percept(self, temperature, is_occupied):
        if not is_occupied:
            target_mode = "ECO"
        elif temperature > 26:
            target_mode = "COOL"
        elif temperature < 20:
            target_mode = "WARM"
        else:
            target_mode = "IDLE"

        if target_mode == self.previous_mode:
            command_sent = False
        else:
            command_sent = True
            self.previous_mode = target_mode
        return target_mode, command_sent
agent = ClassroomAgent()
test_cases = [
    (29, True),
    (29, True),
    (18, True),
    (25, True),
    (22, False)
]
print("Step | Percept (Temp, Occupied) | Target Mode | Command Sent?")
print("-" * 60)
for step, percept in enumerate(test_cases, 1):
    mode, sent = agent.evaluate_percept(percept[0], percept[1])
    print(f"{step:4} | {str(percept):23} | {mode:11} | {str(sent)}")