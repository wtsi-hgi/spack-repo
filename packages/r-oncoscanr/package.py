# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncoscanr(RPackage):
    """Secondary analyses of CNV data (HRD and more)

    The software uses the copy number segments from a text file and identifies all chromosome arms that are globally altered and computes various genome-wide scores. The following HRD scores (characteristic of BRCA-mutated cancers) are included: LST, HR-LOH, nLST and gLOH. the package is tailored for the ThermoFisher Oncoscan assay analyzed with their Chromosome Alteration Suite (ChAS) but can be adapted to any input.
    """

    homepage = "https://github.com/yannchristinat/oncoscanR"
    bioc = "oncoscanR"

    version("1.10.0", commit="2597ce696de108f5b2618d34dffdfce6f128ded2")
    version("1.4.0", commit="6894b0efc3d35e517507e9470717d49e446aee66")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-iranges@2.30:", type=("build", "run"))
    depends_on("r-genomicranges@1.48:", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
