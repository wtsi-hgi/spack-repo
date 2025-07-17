# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCovrna(RPackage):
    """Multivariate Analysis of Transcriptomic Data

    This package provides the analysis methods fourthcorner and RLQ analysis for large-scale transcriptomic data.
    """

    bioc = "covRNA"

    version("1.34.0", commit="591c0e3ad69e314b34491c91d7dd63479c98f080")
    version("1.28.0", commit="db3b68e5b1363f1826f774b7d98ed2802ab6737e")

    depends_on("r-ade4", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-genefilter", type=("build", "run"))
