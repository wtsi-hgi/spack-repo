# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeltagseg(RPackage):
    """deltaGseg

    Identifying distinct subpopulations through multiscale time series analysis
    """

    bioc = "deltaGseg"

    version("1.48.0", commit="109f214f39f9fe8967b1d720a64a2bbc9e9033f8")
    version("1.42.0", commit="fbbf10824efb4ef1fe8045f5cdf133d8f5198f75")

    depends_on("r@2.15.1:", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-changepoint", type=("build", "run"))
    depends_on("r-wavethresh", type=("build", "run"))
    depends_on("r-tseries", type=("build", "run"))
    depends_on("r-pvclust", type=("build", "run"))
    depends_on("r-fbasics", type=("build", "run"))
    depends_on("r-reshape", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
