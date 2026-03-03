# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMokapot(PythonPackage):
    """Mokapot provides fast and flexible semi-supervised learning for
    proteomics peptide detection workflows."""

    homepage = "https://github.com/wfondrie/mokapot"
    pypi = "mokapot/mokapot-0.10.0.tar.gz"

    license("Apache-2.0")

    version("0.10.0", sha256="80e483491a5b2e6a069f561e88176d5751258b89a7147f5d855e3c11461b7c0b")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools@61:", type="build")
    depends_on("py-setuptools-scm@3.4:", type="build")
    depends_on("py-wheel", type="build")

    depends_on("py-numpy@1.18.1:", type=("build", "run"))
    depends_on("py-pandas@1.0.3:", type=("build", "run"))
    depends_on("py-scikit-learn@0.22.1:", type=("build", "run"))
    depends_on("py-numba@0.48:", type=("build", "run"))
    depends_on("py-matplotlib@3.1.3:", type=("build", "run"))
    depends_on("py-lxml@4.6.2:", type=("build", "run"))
    depends_on("py-triqler@0.6.2:", type=("build", "run"))
    depends_on("py-joblib@1.4:", type=("build", "run"))
    depends_on("py-importlib-metadata@5.1.0:", when="^python@:3.7", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        python("-c", "import mokapot")
