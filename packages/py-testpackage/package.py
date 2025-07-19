"""Test package for git PR creation testing."""

from spack.package import *


class PyTestpackage(PythonPackage):
    """A test package for git PR creation testing."""

    homepage = "https://example.com/testpackage"
    url = "https://example.com/testpackage-1.0.0.tar.gz"
    git = "https://github.com/example/testpackage.git"

    version("1.0.0", sha256="1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef")
    version("main", branch="main")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
