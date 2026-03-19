# Copyright 2013-2024 Lawrence Livermore National Security, LLC
# and other Spack Project Developers. See the top-level COPYRIGHT file
# for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class PyLaplaceTorch(PythonPackage):
    """Laplace approximations for deep learning built on top of PyTorch."""

    homepage = "https://github.com/aleximmer/Laplace"
    pypi = "laplace-torch/laplace_torch-0.2.2.2.tar.gz"

    maintainers("softpack-bot")
    license("MIT")

    version("0.2.2.2", sha256="7898a24b7d143bc8f23b69817767277b8d9e260682a62b4d172a58deeed6dd87")
    version("0.2.2.1", sha256="90b9725ac032b23a7d2e1a15698f86b1a8eff9b1714dc9f4e59d73e096ebd1a2")
    version("0.2.2", sha256="1b495c747c6cf62fbc02369c47035746e249b27582010b1f7d0185674f60e70a")
    version("0.2.1", sha256="641823a6d3e1dcb8297202b896ae2969334bf96df9a4a6f8cf688896d67d96f2")
    version(
        "0.1a2",
        sha256="9e9329ad7463eddd3a8c9c0b3647800a8f200886d941ba90a3b664739e4a8500",
        url="https://files.pythonhosted.org/packages/4f/1d/806fc3f8a13b340611954d7afcecd3a6d9cf4c36f8e351ca48d482a525a1/laplace-torch-0.1a2.tar.gz",
    )
    version(
        "0.1a1",
        sha256="022c534d707247fd22a23b3ff33fd65020b6f52ff1a461011b8ea25e67094886",
        url="https://files.pythonhosted.org/packages/8e/33/bcd054eee803e6c4bea20fbb6faf56e431aef0041e974d9af0c1e693b57a/laplace-torch-0.1a1.tar.gz",
    )

    depends_on("python@3.9:", type=("build", "run"), when="@0.2.1:")
    depends_on("python@3.8:", type=("build", "run"), when="@:0.1a2")

    depends_on("py-pdm-backend", type="build")

    depends_on("py-backpack-for-pytorch", type=("build", "run"))
    depends_on("py-asdfghjkl", type=("build", "run"), when="@:0.1a2")
    depends_on("py-asdfghjkl@0.1a4", type=("build", "run"), when="@0.2.1:")
    depends_on("py-curvlinops-for-pytorch@3.0.1:", type=("build", "run"), when="@0.2.1:")
    depends_on("py-numpy", type=("build", "run"), when="@0.2.2:")
    depends_on("py-opt-einsum", type=("build", "run"), when="@0.2.1:")
    depends_on("py-torchmetrics", type=("build", "run"), when="@0.2.1:")
    depends_on("py-torchaudio", type=("build", "run"), when="@:0.2.1")
    depends_on("py-torchvision", type=("build", "run"))
    depends_on("py-torchvision@0.15:", type=("build", "run"), when="@0.2.2:")
    depends_on("py-torch", type=("build", "run"))
    depends_on("py-torch@2:", type=("build", "run"), when="@0.2.1:")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import laplace")
