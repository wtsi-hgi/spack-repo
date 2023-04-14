# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcppHnsw(RPackage):
    """Rcpp' Bindings for 'hnswlib.

    'Hnswlib' is a C++ library for Approximate Nearest Neighbors. This ppackage
    provides a minimal R interface by relying on the 'Rcpp' package. See
    <https://github.com/nmslib/hnswlib> for more on 'hnswlib'. 'hnswlib' is
    released under Version 2.0 of the Apache License."""

    cran = "RcppHNSW"

    version("0.4.1", sha256="4f0082154f77dcb7756d41cdbfe0f58316431b9027081321a27942f319097c74")

    depends_on("r-rcpp", type=("build", "run"))
