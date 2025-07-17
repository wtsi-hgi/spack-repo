# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcmetrics(RPackage):
    """A Framework for Quality Control

    The package provides a framework for generic quality control of data. It permits to create, manage and visualise individual or sets of quality control metrics and generate quality control reports in various formats.
    """

    homepage = "http://lgatto.github.io/qcmetrics/articles/qcmetrics.html"
    bioc = "qcmetrics"

    version("1.46.0", commit="ba43f30593db4353cfad6da044a4c2b6642539a2")
    version("1.40.1", commit="ef898de6d318ae553f0f756445ac3ac06592bcdf")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-xtable", type=("build", "run"))
    depends_on("r-pander", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
