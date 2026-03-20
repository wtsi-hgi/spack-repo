# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyBackpackForPytorch(PythonPackage):
    """BackPACK adds second-order information and utility layers to PyTorch."""

    homepage = "https://backpack.pt/"
    pypi = "backpack-for-pytorch/backpack_for_pytorch-1.7.1.tar.gz"

    maintainers("softpack-bot")
    license("MIT")
    import_modules = ["backpack"]

    version("1.7.1", sha256="edfe332e4b06a69073a6d857c5fd08d286c020be4d411f5c50a729f26f62a30d")
    version("1.6.0", sha256="af6495b71bacf82a1c7cab01aa85bebabccfe74d87d89f108ea72a4a0d384de3")

    depends_on("python@3.9:", type=("build", "run"), when="@1.7:")
    depends_on("python@3.8:", type=("build", "run"), when="@:1.6.0")

    depends_on("py-setuptools@61:", type="build", when="@1.7:")
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")

    depends_on("py-torch@2.2:", type=("build", "run"), when="@1.7:")
    depends_on("py-torch@1.9:", type=("build", "run"), when="@:1.6.0")

    depends_on("py-torchvision@0.7:", type=("build", "run"))
    depends_on("py-einops@0.3:0.999", type=("build", "run"))
    depends_on("py-unfoldnd@0.2:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import backpack")
