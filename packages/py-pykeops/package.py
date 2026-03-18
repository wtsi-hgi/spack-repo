# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPykeops(PythonPackage):
    """Python bindings for KeOps (Kernel Operations) with autodiff and GPU support."""

    homepage = "https://www.kernel-operations.io/"
    pypi = "pykeops/pykeops-2.3.tar.gz"

    license("MIT")

    version("2.3", sha256="458fa77985efd2161be9c719e8dd41e495526cd735d3262aec09902505f5bdba")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pybind11", type=("build", "run"))
    depends_on("py-keopscore@2.3", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = which("python")
            python("-c", "import pykeops")
