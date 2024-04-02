import os
from pathlib import Path

import pytest
from metalib2 import Metadata


@pytest.fixture(scope='function')
def sample_data():
    """Loads sample metadata"""
    # setup environment variable used by sample data
    os.environ['RAW_DATA_PATH'] = '.'

    # load sample data
    filename = Path(__file__).parent / 'data/2023-10-10.yaml'
    metadata = Metadata.load_yaml(filename)
    return metadata
