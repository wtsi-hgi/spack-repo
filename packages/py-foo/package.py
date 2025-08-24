from spack.package import *


class PyFoo(PythonPackage):
    """Placeholder recipe for the 'foo' Python package from PyPI."""

    homepage = "https://example.com"
    pypi = "foo/foo-.1.tar.gz"

    # PyPI lists version ".1" but provides no sdist artifacts
    version(".1", sha256="0000000000000000000000000000000000000000000000000000000000000000")

    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import foo")

