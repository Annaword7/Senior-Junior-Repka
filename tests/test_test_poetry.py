from senior_junior_repka import __version__
import senior_junior_repka


def test_version():
    assert __version__ == '0.1.0'

def test_increase():
    # self.assertEqual(senior_junior_repka.increase(2), 3)
    assert senior_junior_repka.increase(2) == 3
    
def test_decrease():
    # self.assertEqual(senior_junior_repka.decrease(2), 1)
    assert senior_junior_repka.decrease(2) == 1
