from app.process_monitor import get_top_processes


def test_process_list_returns_data():

    processes = get_top_processes()

    assert isinstance(processes, list)


def test_process_data_structure():

    processes = get_top_processes()

    if processes:

        process = processes[0]

        assert "pid" in process
        assert "name" in process
        assert "cpu" in process
        assert "memory" in process


def test_process_limit():

    processes = get_top_processes()

    assert len(processes) <= 5