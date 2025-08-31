# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOsServiceTypes(PythonPackage):
    """Python library for consuming OpenStack sevice-types-authority data"""

    homepage = "https://docs.openstack.org/os-service-types/"
    pypi = "os-service-types/os-service-types-1.7.0.tar.gz"

    maintainers("haampie")

    # Use legacy setuptools install to avoid wheel build issues
    use_pip = False

    version("1.7.0", sha256="31800299a82239363995b91f1ebf9106ac7758542a1e4ef6dc737a5932878c6c")

    depends_on("python@2.7:2.8,3.5:", type=("build", "run"))
    depends_on("py-pbr@2.0.0:2.0,2.1.1:", type=("build", "run"))
    # Newer setuptools versions removed the 'bdist_wininst' command, which causes
    # old pbr/setup.cfg setups to fail during wheel builds. Constrain to a
    # compatible setuptools to build from source successfully.
    depends_on("py-setuptools@:57.4", type="build")
    # pbr uses pkg_resources at runtime
    depends_on("py-setuptools@:57.4", type="run")

    def patch(self):
        # Old setuptools removed 'bdist_wininst'. Some legacy setup flows still
        # probe it during wheel/installation steps. Inject a harmless stub
        # implementation so any lookups succeed on non-Windows platforms.
        filter_file(
            "import setuptools",
            (
                "import setuptools\n"
                "from setuptools import Command\n"
                "import sys, types\n"
                "import distutils.command\n"
                "# Provide a dummy distutils.command.bdist_wininst module\n"
                "bdist_wininst_mod = types.ModuleType('distutils.command.bdist_wininst')\n"
                "class bdist_wininst(Command):\n"
                "    user_options = []\n"
                "    def initialize_options(self): pass\n"
                "    def finalize_options(self): pass\n"
                "    def run(self): pass\n"
                "bdist_wininst_mod.bdist_wininst = bdist_wininst\n"
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

    def install(self, spec, prefix):
        # Avoid pip/wheel path which triggers deprecated Windows-only commands
        with working_dir(self.stage.source_path):
            python("setup.py", "install", f"--prefix={prefix}")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python('-c', 'import os_service_types')
