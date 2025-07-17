# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrichDmelanogasterBackground(RPackage):
    """D. melanogaster background for PWMEnrich

    PWMEnrich pre-compiled background objects for Drosophila melanogaster and MotifDb D. melanogaster motifs.
    """

    bioc = "PWMEnrich.Dmelanogaster.background"

    version("4.42.0", commit="cad267fb1b18d3871f5b73967545732a836c76cc")
    version("4.36.0", commit="22c7fe3170e802778bd03ad00359c9875ac76216")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-pwmenrich", type=("build", "run"))
