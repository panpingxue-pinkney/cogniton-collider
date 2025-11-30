# launcher/emitter.py
# Simulates the emission of new Cogniton vectors into the stream.

import numpy as np
import uuid
import time

def emit_cogniton(count: int):
    """Generates 'count' dummy Cogniton vectors and saves them to the stream DB."""
    print(f"[{time.ctime()}] Simulating {count} Cogniton emissions...")
    
    for i in range(count):
        # Generate a dummy vector (e.g., 768 dimensions for quick demo)
        vector = np.random.rand(768) 
        cogniton_id = str(uuid.uuid4())
        
        # In v0.1, we just print the emission
        print(f"Emitted Cogniton ID: {cogniton_id[:8]}... | Neg-Entropy: {np.sum(vector):.2f}")
        
    print("Emission simulation complete. Ready for collision.")

if __name__ == '__main__':
    # Simple argument parser for --count 50
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--count', type=int, default=50, help='Number of Cognitons to emit.')
    args = parser.parse_args()
    
    emit_cogniton(args.count)