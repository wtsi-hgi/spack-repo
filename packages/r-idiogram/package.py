# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdiogram(RPackage):
    """idiogram

    A package for plotting genomic data by chromosomal location
    """

    bioc = "idiogram"

    version("1.84.0", commit="fe94a95ba786853ad9ea4e6731bac9ce1f482e06")
    version("1.78.0", commit="1563def5fd989222cd15410160921bda9788ae31")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-annotate", type=("build", "run"))
    depends_on("r-plotrix", type=("build", "run"))
