# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REds(RPackage):
    """eds: Low-level reader for Alevin EDS format

    This packages provides a single function, readEDS. This is a low-level utility for reading in Alevin EDS format into R. This function is not designed for end-users but instead the package is predominantly for simplifying package dependency graph for other Bioconductor packages.
    """

    homepage = "https://github.com/mikelove/eds"
    bioc = "eds"

    version("1.10.0", commit="6b77a2e9eeb4296d92900a16ba274284d3b43944")
    version("1.4.0", commit="0cfd0366b2fb2ab55ef926054126f6835a79b873")

    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("zlib", type=("build", "link", "run"))
