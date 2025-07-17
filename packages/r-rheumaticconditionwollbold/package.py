# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRheumaticconditionwollbold(RPackage):
    """Normalized gene expression dataset published by Wollbold et al. [2009] (WOLLBOLD).

    Normalized gene expression data from rheumatic diseases from study published by Wollbold et al. in 2009, provided as an eSet.
    """

    homepage = "http://compbio.dfci.harvard.edu/"
    bioc = "rheumaticConditionWOLLBOLD"

    version("1.46.0", commit="56fba5ff5cca9a54edcde2a21091e2a8a281dc28")
    version("1.40.0", commit="f646b035a6f6e3439dd0b1ea6e38c51abd36d41f")

    depends_on("r@2.10:", type=("build", "run"))
