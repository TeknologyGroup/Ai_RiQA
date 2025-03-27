# tests/test_simulation.py
def test_simulation():
    params = SimulationParameters(time_range=(0, 5), k=2.0)
    result = simulate_complex_system(params)
    assert len(result['time']) == 100
    assert len(result['energy']) == 100
