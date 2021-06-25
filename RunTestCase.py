import  sys
import pytest

from config.conf import ROOT_DIR

def main():
	if ROOT_DIR not in sys.path:
			sys.path.append(ROOT_DIR)

if __name__ == '__main__':
	main()