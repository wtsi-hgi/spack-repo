# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTorchinfo(PythonPackage):
    """Model summary in PyTorch, based off of the original torchsummary."""

    homepage = "https://github.com/tyleryep/torchinfo"
    pypi = "torchinfo/torchinfo-1.8.0.tar.gz"

    license("MIT")

    version("1.8.0", sha256="72e94b0e9a3e64dc583a8e5b7940b8938a1ac0f033f795457f27e6f4e7afa2e9")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-torch", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python(
                "-c",
                "import torchinfo"
            )
