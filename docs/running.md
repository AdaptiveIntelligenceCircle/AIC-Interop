# Running the reference client

```bash
cd reference/python
PYTHONPATH=. python3 examples/bridge_demo.py
PYTHONPATH=. python3 -m pytest tests/ -q
```

Optional:

```bash
python3 -c "from aic_interop import BridgePolicy; b=BridgePolicy({'net0','net1'}); print(b.send('net0','net1',{}))"
```

No network ports are opened by default.  
Everything runs in-process.