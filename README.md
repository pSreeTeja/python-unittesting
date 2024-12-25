Procedure for writing a Test Case using **unittest** in python 
create a class for the logic you want to write unit tests for

     import unittest
     from unnittest.mock import patch
     from src.utility.logic import mylogic
     
     class TestMylogic(unittest.TestCase):
       @patch('src.utility.logic.mylogic.logging.logger.info")
       def test_mymethodinside_my_logic(self, mock_logger_info):
         *assert statements*
         eg:
         1) mock_logger_info.assert_called_with("Started My Logic")
         2) with self.assertRaises(TechnicalException):
               myLogic(event)
        
         
