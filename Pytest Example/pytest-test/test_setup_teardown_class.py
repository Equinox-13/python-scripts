# Execute using "pytest -v -s"

class TestClass:

    @classmethod
    def setup_class(self):
        print("\nSetup Class")

    @classmethod
    def teardown_class(self):
        print("\nTeardown Class")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unknown test")

    def teardown_method(self, method):
        if method == self.test2:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unknown test")

    def test1(self):
        print("\nExecuting test1")
        assert True

    def test2(self):
        print("\nExecuting test2")
        assert True
