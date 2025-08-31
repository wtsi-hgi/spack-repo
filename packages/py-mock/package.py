from spack.package import *


class PyMock(PythonPackage):
    """mock is a library for testing in Python. It allows you to replace parts
    of your system under test with mock objects and make assertions about
    how they have been used."""

    homepage = "https://github.com/testing-cabal/mock"
    pypi = "mock/mock-4.0.3.tar.gz"

    # Known releases used in environments
    version("4.0.3", sha256="7d3fbbde18228f4ff2f1f119a45cdffa458b4c0dee32eb4d2bb2f82554bac7bc")
    version("3.0.5", sha256="83657d894c90d5681d62155c82bda9c1187827525880eda8ff5df4ec813437c3")
    version("3.0.3", sha256="5eda46efb363128828d6fd2bf8d16f6ebb66f5b543b9f7f8f4eb224c5cb503fe")
    version("2.0.0", sha256="b158b6df76edd239b8208d481dc46b6afd45a846b7812ff0ce58971cf5bc8bba")
    version("1.3.0", sha256="1e247dbecc6ce057299eb7ee019ad68314bb93152e81d9a6110d35f4d5eca0f6")

    # Build dependencies
    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip", type="build")
    depends_on("py-wheel", type="build")
    depends_on("py-pbr", type=("build", "run"))

    # Runtime dependency
    depends_on("py-six", type=("build", "run"))

    # Older releases require setuptools providing bdist_wininst; cap to avoid failures
    depends_on("py-setuptools@:57", when="@:2.0.0", type="build")

    def patch(self):
        # Older sdist attempts to use the deprecated/Windows-only bdist_wininst command
        # Inject a no-op implementation to avoid failures on non-Windows platforms.
        if self.spec.satisfies("@:2.0.0"):
            filter_file(
                "import setuptools",
                (
                    "import setuptools\n"
                    "from setuptools import Command\n"
                    "import sys, types\n"
                    "\n"
                    "# Provide a dummy distutils.command.bdist_wininst module\n"
                    "bdist_wininst_mod = types.ModuleType('distutils.command.bdist_wininst')\n"
                    "class bdist_wininst(Command):\n"
                    "    user_options = []\n"
                    "    def initialize_options(self): pass\n"
                    "    def finalize_options(self): pass\n"
                    "    def run(self): pass\n"
                    "bdist_wininst_mod.bdist_wininst = bdist_wininst\n"
                    "sys.modules.setdefault('distutils', types.ModuleType('distutils'))\n"
                    "sys.modules.setdefault('distutils.command', types.ModuleType('distutils.command'))\n"
                    "sys.modules['distutils.command.bdist_wininst'] = bdist_wininst_mod\n"
                ),
                "setup.py",
                string=True,
            )
            filter_file(
                "setuptools.setup(",
                "setuptools.setup(cmdclass={'bdist_wininst': bdist_wininst}, ",
                "setup.py",
                string=True,
            )
            # Note: avoid creating a local 'distutils' package to not shadow stdlib

    def install(self, spec, prefix):
        # For old releases, avoid pip/wheel entirely as wheel build trips over
        # deprecated Windows-only commands. Do a classic setuptools install.
        if spec.satisfies("@:2.0.0"):
            with working_dir(self.stage.source_path):
                python("setup.py", "install", f"--prefix={prefix}")
        else:
            # Defer to the standard pip-based install for newer releases
            from spack.build_systems.python import PythonPipBuilder

            pip(*PythonPipBuilder.std_args(self), f"--prefix={prefix}", ".")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # Basic import test
            python("-c", "import mock; print(mock.__version__)")
