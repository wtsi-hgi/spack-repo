# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyEpik(PythonPackage):
    """Epistatic Kernels for GPU-accelerated Gaussian process regression."""

    homepage = "https://github.com/cmarti/epik"
    pypi = "epik/epik-0.1.0.tar.gz"

    license("MIT")

    version("0.1.0", sha256="c0b95f81dfcd634e4f58f4eb7d596de2b08eae1a8d141edb0b560eb91f6c2b51")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-gpytorch@1.11:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-pykeops", type=("build", "run"))
    depends_on("py-torch@2:", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = which("python")
            python("-c", "import epik")
