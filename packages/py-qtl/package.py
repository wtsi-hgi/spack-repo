# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyQtl(PythonPackage):
    """pyQTL is a python module for analyzing and visualizing quantitative trait loci (QTL) data."""

    homepage = "https://github.com/broadinstitute/pyqtl"
    pypi = "qtl/qtl-0.1.8.tar.gz"

    version("0.1.10", sha256="7de75e407627052ba8b74e60ebeebe0e9e911140c58d2026047f0057642e353c")
    version("0.1.8", sha256="8fdb99cda1ceff578a233db6c15a944fa57b43a2826af41c292e36848906117b")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools@61:", when="@0.1.10:", type="build")

    with default_args(type=("build", "run")):
        depends_on("py-numpy")
        depends_on("py-numpy@:1", when="@:0.1.8")
        depends_on("py-pandas")
        depends_on("py-scipy")
        depends_on("py-matplotlib")
        depends_on("py-seaborn")
        depends_on("py-pybigwig")
        depends_on("py-bx-python")
