# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDmrcaller(RPackage):
    """Differentially Methylated Regions caller

    Uses Bisulfite sequencing data in two conditions and identifies differentially methylated regions between the conditions in CG and non-CG context. The input is the CX report files produced by Bismark and the output is a list of DMRs stored as GRanges objects.
    """

    bioc = "DMRcaller"

    version("1.40.0", commit="ff43cc9bf1c2a32dc6cee6723def0c69e3036353")
    version("1.34.0", commit="7b214e9051c4367e36d3be1fe7b6d59b95fe1364")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-rcpproll", type=("build", "run"))
    depends_on("r-betareg", type=("build", "run"))
