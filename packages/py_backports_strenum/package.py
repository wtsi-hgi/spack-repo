# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBackportsStrenum(PythonPackage):
    """Backport of Python's StrEnum for earlier interpreters."""

    homepage = "https://github.com/clbarnes/backports.strenum"
    pypi = "backports.strenum/backports_strenum-1.3.1.tar.gz"

    license("MIT")

    version("1.3.1", sha256="77c52407342898497714f0596e86188bb7084f89063226f4ba66863482f42414")

    depends_on("py-setuptools", type="build")
    depends_on("py-poetry-core@1:", type="build")
    depends_on("python@3.8.6:3.10.99", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import backports.strenum")
