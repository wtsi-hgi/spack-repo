# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyTspex(PythonPackage):
    """tspex is a tissue-specificity calculator tool. It provides both an easy-to-use object-oriented Python API and a command-line interface (CLI) for calculating a variety of tissue-specificity metrics from gene expression data."""

    homepage = "https://apcamargo.github.io/tspex/"
    pypi = "tspex/tspex-0.6.3.tar.gz"

    version("0.6.3", sha256="315bfa1f60ea582777c549313cad9e9da0a4d11c5f69a6fc767bd0823dc46316")

    depends_on("py-matplotlib@2.2:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas@0.23:", type=("build", "run"))
    depends_on("py-xlrd@1.1.0:", type=("build", "run"))
