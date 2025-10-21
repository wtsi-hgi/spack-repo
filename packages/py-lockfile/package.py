# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLockfile(PythonPackage):
    """The lockfile package exports a LockFile class which provides a
    simple API for locking files. Unlike the Windows msvcrt.locking
    function, the fcntl.lockf and flock functions, and the
    deprecated posixfile module, the API is identical across both
    Unix (including Linux and Mac) and Windows platforms. The lock
    mechanism relies on the atomic nature of the link (on Unix) and
    mkdir (on Windows) system calls. An implementation based on
    SQLite is also provided, more as a demonstration of the
    possibilities it provides than as production-quality code.
    """

    pypi = "lockfile/lockfile-0.10.2.tar.gz"
    homepage = "https://launchpad.net/pylockfile"

    license("MIT")

    # Avoid pip/wheel path which triggers deprecated Windows-only commands
    # in legacy setups; use direct setuptools install instead.
    use_pip = False

    version("0.12.2", sha256="6aed02de03cba24efabcd600b30540140634fc06cfa603822d508d5361e9f799")
    version("0.10.2", sha256="9e42252f17d1dd89ee31745e0c4fbe58862c25147eb0ef5295c9cd9bcb4ea2c1")

    depends_on("py-setuptools", type="build")
    depends_on("py-pbr", type="build")
    depends_on("py-pbr@1.8:", type="build", when="@0.12.2:")

    def patch(self):
        # Old setuptools removed 'bdist_wininst'. Some legacy setup flows still
        # probe it during builds. Provide a harmless stub so lookups succeed on
        # non-Windows platforms and avoid failures during script installation.
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
                "# Also provide setuptools.command.bdist_wininst to satisfy setuptools entrypoint\n"
                "setuptools_bdist_wininst = types.ModuleType('setuptools.command.bdist_wininst')\n"
                "setattr(setuptools_bdist_wininst, 'bdist_wininst', bdist_wininst)\n"
                "sys.modules['setuptools.command.bdist_wininst'] = setuptools_bdist_wininst\n"
                "# Shim missing easy_install.get_script_header removed in newer setuptools\n"
                "from setuptools.command import easy_install as _easy_install\n"
                "if not hasattr(_easy_install, 'get_script_header'):\n"
                "    def get_script_header(script_text, executable, is_wininst):\n"
                "        shebang = f'#!{executable}\\n' if executable else '#!/usr/bin/env python\\n'\n"
                "        return shebang\n"
                "    _easy_install.get_script_header = get_script_header\n"
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
        # Perform a legacy setuptools install to avoid wheel build path
        with working_dir(self.stage.source_path):
            python("setup.py", "install", f"--prefix={prefix}")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            # lockfile has no CLI; verify basic import
            python('-c', 'import lockfile')
