# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaschyhs(RPackage):
    """ExpressionSet for response of yeast to heat shock and other environmental stresses

    Data from PMID 11102521
    """

    homepage = (
        "http://genome-www.stanford.edu/yeast_stress/data/rawdata/complete_dataset.txt"
    )
    bioc = "gaschYHS"

    version("1.46.0", commit="940087669a0f6b60dde17ebeb133c034135fb971")
    version("1.40.0", commit="3d9da0e0e594fdcd60f87ae86e524b50f4f86466")

    depends_on("r@2.14:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
