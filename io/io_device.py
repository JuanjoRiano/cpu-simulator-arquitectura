# io/io_device.py

import time
import threading
from queue import Queue

class IODevice:
    def __init__(self, name, latency_ms=50):
        self.name = name
        self.latency_ms = latency_ms
        self.queue = Queue()
        self.interrupt = False
        self._running = True

        self._worker = threading.Thread(target=self._process_requests)
        self._worker.daemon = True
        self._worker.start()

    def request_read(self, address):
        self.queue.put(("read", address, None))

    def request_write(self, address, data):
        self.queue.put(("write", address, data))

    def _process_requests(self):
        while self._running:
            if not self.queue.empty():
                op_type, addr, data = self.queue.get()
                print(f"[{self.name}] Procesando {op_type.upper()} en dirección {hex(addr)}")
                time.sleep(self.latency_ms / 1000)
                self.interrupt = True
            time.sleep(0.001)

    def check_interrupt(self):
        if self.interrupt:
            self.interrupt = False
            return True
        return False

    def shutdown(self):
        self._running = False
        self._worker.join()

# --- Prueba directa ---
if __name__ == "__main__":
    device = IODevice("Disk", latency_ms=200)
    device.request_write(0x1000, 42)
    device.request_read(0x2000)

    print("Esperando interrupciones...")
    while True:
        if device.check_interrupt():
            print("¡Interrupción recibida!")
            break
        time.sleep(0.01)

    device.shutdown()
    print("Simulación finalizada.")