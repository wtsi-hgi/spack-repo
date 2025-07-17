# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcdata(RPackage):
    """Data for Combination Connectivity Mapping (ccmap) Package

    This package contains microarray gene expression data generated from the Connectivity Map build 02 and LINCS l1000. The data are used by the ccmap package to find drugs and drug combinations to mimic or reverse a gene expression signature.
    """

    bioc = "ccdata"

    version("1.34.0", commit="21cb7c92e05765158bf56effb61cfee04abc40f0")
    version("1.28.0", commit="93125e53e8ae9370742c2c1aaab74fbeac60ce1c")

    depends_on("r@3.3:", type=("build", "run"))
