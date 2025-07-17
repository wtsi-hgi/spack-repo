# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancervdx(RPackage):
    """Gene expression datasets published by Wang et al. [2005] and Minn et al. [2007] (VDX).

    Gene expression data from a breast cancer study published by Wang et al. in 2005 and Minn et al. in 2007, provided as an eSet.
    """

    homepage = "http://compbio.dfci.harvard.edu/"
    bioc = "breastCancerVDX"

    version("1.46.0", commit="fd1a1eeaeeb53e9b6e036cd7f98e777341c8dc5c")
    version("1.40.0", commit="cee47a68981fb6f90610fc8b45392d1c000af29f")

    depends_on("r@2.5:", type=("build", "run"))
