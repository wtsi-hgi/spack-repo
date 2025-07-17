# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarbchip(RPackage):
    """Experimental Data Package: harbChIP

    data from a yeast ChIP-chip experiment
    """

    bioc = "harbChIP"

    version("1.46.0", commit="8aa02dca7ee126d5a80e855af7b5afba721bf7cb")
    version("1.40.0", commit="8611d179015e38dc49897a5951ddc897f5567e99")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
