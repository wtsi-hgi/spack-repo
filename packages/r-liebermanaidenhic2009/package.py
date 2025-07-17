# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiebermanaidenhic2009(RPackage):
    """Selected data from the HiC paper of E. Lieberman-Aiden et al. in Science (2009)

    This package provides data that were presented in the article "Comprehensive mapping of long-range interactions reveals folding principles of the human genome", Science 2009 Oct 9;326(5950):289-93. PMID: 19815776
    """

    bioc = "LiebermanAidenHiC2009"

    version("0.46.0", commit="e2a53b6c70c1dd6003bd30258e3128dee62e29de")
    version("0.40.0", commit="b1733c6cbd1baa0d4cf76672cee78e58b1197309")

    depends_on("r-kernsmooth", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
