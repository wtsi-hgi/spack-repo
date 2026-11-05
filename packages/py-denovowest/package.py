# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDenovowest(PythonPackage):
    """De novo mutation simulation framework."""

    homepage = "https://hurlesgroupsanger.github.io/DeNovoWEST/"
    pypi = "denovowest/denovowest-0.2.0.tar.gz"

    license("MIT")

    version("0.2.0", sha256="af0ee5c85e6b1a7c86b46883a2ce918e81b866972c5d46152d7d99258c61ea9e")

    depends_on("py-setuptools@61:", type="build")
    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pandas", type=("build", "run"))
    depends_on("py-gffutils", type=("build", "run"))
    depends_on("py-click", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-pysam", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
    depends_on("py-pyfaidx", type=("build", "run"))
    depends_on("py-jinja2", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            Executable(join_path(self.prefix.bin, "denovowest"))("--help")
