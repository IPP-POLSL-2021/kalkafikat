class DD12QueueSimulation:
    def __init__(self, add_interval, remove_interval, queue_capacity):
        self.add_interval = add_interval  # Co ile cykli dodawany jest nowy element
        # Co ile cykli usuwany jest pierwszy element
        self.remove_interval = remove_interval
        self.queue_capacity = queue_capacity  # Pojemność kolejki
        self.queue = []
        self.loss_counter = 0
        self.cycle_count = 0

    def add_element(self):
        self.queue.append("New Element")

    def remove_element(self):
        if self.queue:
            self.queue.pop(0)
        else:
            self.loss_counter += 1

    def simulate_queue(self, num_cycles):
        for _ in range(num_cycles):
            self.cycle_count += 1

            if (self.cycle_count % self.add_interval == 0) and len(self.queue) < self.queue_capacity:
                self.add_element()

            if self.cycle_count % self.remove_interval == 0:
                self.remove_element()

            # Przesunięcie wszystkich elementów o jeden, jeśli kolejka jest pełna
            if len(self.queue) == self.queue_capacity:
                self.loss_counter += 1
                # self.queue = self.queue[1:] + ["New Element"]

            print("\nCycle:", self.cycle_count)
            print("Queue:", self.queue)
            print("Loss Counter:", self.loss_counter)


if __name__ == "__main__":
    num_cycles = 30
    add_interval = 3
    remove_interval = 5
    queue_capacity = 3

    dd12_queue_simulation = DD12QueueSimulation(
        add_interval, remove_interval, queue_capacity)
    dd12_queue_simulation.simulate_queue(num_cycles)
