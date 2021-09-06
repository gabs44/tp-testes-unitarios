from unittest import main
from unittest.case import TestCase
from unittest.mock import MagicMock, Mock, patch

from conta import Conta


class TestConta(TestCase):

    @patch('builtins.print')
    def test_extrato(self, mock_print):
        conta = Conta(1, 'Fulano', 200, 500)
        conta.extrato()
        mock_print.assert_called_with(200)

if __name__ == '__main__':
    main()