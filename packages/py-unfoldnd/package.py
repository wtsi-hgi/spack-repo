# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyUnfoldnd(PythonPackage):
    """N-dimensional unfold (im2col) and fold (col2im) utilities for PyTorch."""

    homepage = "https://github.com/f-dangel/unfoldNd"
    pypi = "unfoldnd/unfoldNd-0.2.3.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["unfoldNd"]

    version("0.2.3", sha256="f5b5121d05dafdd70e873ac64a3ecdadfc4c0e8840a0facc86986ede664ab188")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
    depends_on("py-packaging", type=("build", "run"))

    depends_on("py-torch", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import unfoldNd")
