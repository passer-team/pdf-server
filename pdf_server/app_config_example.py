from os.path import abspath

# IS_DEV = False
IS_DEV = True
IS_DOCKER = True
LISTEN_PORT = 50054
WORKPLACE = abspath("../workplace")
TEST_DIR = abspath("../tests/test-data")
FONTS_PATH = abspath("../workplace/fonts")
PDF_SCRIPT = abspath("./pdf.js")
CHUNK_SIZE = 2 * 1024 * 1024
