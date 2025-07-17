# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghmcr(RPackage):
    """Find chromosome regions showing common gains/losses

    This package provides functions to identify genomic regions of interests based on segmented copy number data from multiple samples.
    """

    bioc = "cghMCR"

    version("1.66.0", commit="5c037e56e40d494bbee947b4e1b18d0e7bf166e0")
    version("1.60.0", commit="f965259ceb59d5f7b3104ced7782cd546987e9cf")

    depends_on("r-dnacopy", type=("build", "run"))
    depends_on("r-cntools", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biocgenerics@0.1.6:", type=("build", "run"))
