# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyKeopscore(PythonPackage):
    """KeOps meta-programming engine used through bindings such as PyKeOps."""

    homepage = "https://github.com/getkeops/keops"
    pypi = "keopscore/keopscore-2.3.tar.gz"

    license("MIT")

    version("2.3", sha256="e8a700c22efee59a7723ed7516c2d88ab143a11290dd23b07eb7bba1c9d16fef")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python = which("python")
            python("-c", "import keopscore")
