# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDndscv(RPackage):
    """The dNdScv R package is a group of maximum-likelihood dN/dS methods designed to quantify selection in cancer and somatic evolution (Martincorena et al., 2017)."""

    homepage = "https://www.sanger.ac.uk/tool/dndscv/"
    git = "https://github.com/im3sanger/dndscv"

	version("2023-09-29", commit="ae10c765ecb6b3a6ff06cd5a50aadc317dab2289")

    depends_on("r-seqinr", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-poilog", type=("build", "run"))
    depends_on("r-plyr", type=("build", "run"))
