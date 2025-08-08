# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsvadata(RPackage):
    """Data employed in the vignette of the GSVA package

    This package stores the data employed in the vignette of the GSVA package. These data belong to the following publications: Armstrong et al. Nat Genet 30:41-47, 2002; Cahoy et al. J Neurosci 28:264-278, 2008; Carrel and Willard, Nature, 434:400-404, 2005; Huang et al. PNAS, 104:9758-9763, 2007; Pickrell et al. Nature, 464:768-722, 2010; Skaletsky et al. Nature, 423:825-837; Verhaak et al. Cancer Cell 17:98-110, 2010
    """

    bioc = "GSVAdata"

    version("1.44.0", commit="7cb2abf0e70788e4e67bd6706395ed44467240d6")
    version("1.38.0", commit="196f501bd9eecda6c783898c090dd67c9bab56d2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-hgu95a-db", type=("build", "run"))
