# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancerupp(RPackage):
    """Gene expression dataset published by Miller et al. [2005] (UPP).

    Gene expression data from a breast cancer study published by Miller et al. in 2005, provided as an eSet.
    """

    homepage = "http://compbio.dfci.harvard.edu/"
    bioc = "breastCancerUPP"

    version("1.46.0", commit="07e2ecb42d51aae8d680cdd126aa58d86402fed5")
    version("1.40.0", commit="542412f31f9c070b0e8ef2def6153be3b6f4ad45")

    depends_on("r@2.5:", type=("build", "run"))
