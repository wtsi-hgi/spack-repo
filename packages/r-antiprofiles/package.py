# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAntiprofiles(RPackage):
    """Implementation of gene expression anti-profiles

    Implements gene expression anti-profiles as described in Corrada Bravo et al., BMC Bioinformatics 2012, 13:272 doi:10.1186/1471-2105-13-272.
    """

    homepage = "https://github.com/HCBravoLab/antiProfiles"
    bioc = "antiProfiles"

    version("1.48.0", commit="949bbab685ed0ccbc3e0867364044cada0de937d")
    version("1.42.0", commit="cad816f3b23c95fc4bc950d5733bc767b6b8167d")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-matrixstats@0.50:", type=("build", "run"))
    depends_on("r-locfit@1.5:", type=("build", "run"))
