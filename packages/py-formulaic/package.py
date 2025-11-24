# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT
# file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFormulaic(PythonPackage):
    """High-performance implementation of Wilkinson formulas for Python."""

    homepage = "https://matthewwardrop.github.io/formulaic"
    pypi = "formulaic/formulaic-1.2.1.tar.gz"

    license("MIT")

    version("1.2.1", sha256="dc79476baa2d811b35798893eb2f2c1e51edee8d7a9c1429b400e56f4e0beccc")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-hatchling", type="build")
    depends_on("py-hatch-vcs", type="build")

    depends_on("py-interface-meta@1.2:", type=("build", "run"))
    depends_on("py-narwhals@1.17:", type=("build", "run"))
    depends_on("py-numpy@1.20:", type=("build", "run"))
    depends_on("py-pandas@1.3:", type=("build", "run"))
    depends_on("py-scipy@1.6:", type=("build", "run"))
    depends_on("py-typing-extensions@4.2:", type=("build", "run"))
    depends_on("py-wrapt@1:", type=("build", "run"))
    depends_on("py-wrapt@1.17:", type=("build", "run"), when="^python@3.13:")

    @run_after("install")
    def install_test(self):
        """Light-weight import test to ensure the module loads."""
        python = self.spec["python"].command
        with working_dir("spack-test", create=True):
            python("-c", "import formulaic")
