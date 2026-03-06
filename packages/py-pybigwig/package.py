# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from spack.util.executable import ProcessError


class PyPybigwig(PythonPackage):
    """A package for accessing bigWig files using libBigWig."""

    pypi = "pyBigWig/pyBigWig-0.3.4.tar.gz"

    license("MIT")

    version("0.3.12", sha256="e01991790ece496bf6d3f00778dcfb136dd9ca0fd28acc1b3fb43051ad9b8403")
    version("0.3.4", sha256="8c97a19218023190041c0e426f1544f7a4944a7bb4568faca1d85f1975af9ee2")

    variant("numpy", default=True, description="Enable support for numpy integers and vectors")

    # depends_on("c", type="build")  # generated

    depends_on("curl", type=("build", "link", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"), when="+numpy")

    def patch(self):
        if self.spec.satisfies("@:0.3.12 ^python@3:"):
            filter_file(
                "foo = foo.strip().split()",
                "foo = foo.decode().strip().split()",
                "setup.py",
                string=True,
            )

    def setup_build_environment(self, env):
        """Select the distutils implementation dynamically.

        Some Python builds (including newer ones) no longer ship stdlib
        ``distutils`` modules, which causes numpy.distutils to fail when it tries
        to import ``distutils.msvccompiler``.  We probe the build Python and fall
        back to the vendored setuptools implementation when the stdlib module is
        missing.
        """

        python = self.spec["python"].command

        try:
            python("-c", "import distutils.msvccompiler")
        except ProcessError:
            env.set("SETUPTOOLS_USE_DISTUTILS", "local")
        else:
            env.set("SETUPTOOLS_USE_DISTUTILS", "stdlib")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = self.spec["python"].command
            python("-c", "import pyBigWig")
