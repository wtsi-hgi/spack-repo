# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylmnm(RPackage):
    """detect different methylation level (DMR)

    To give the exactly p-value and q-value of MeDIP-seq and MRE-seq data for different samples comparation.
    """

    bioc = "methylMnM"

    version("1.46.0", commit="23872826a245c64337ce5f94d938711677068bd0")
    version("1.40.0", commit="3381d3f4de23eac155886fe9644fe0e0be025205")

    depends_on("r@2.12.1:", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-statmod", type=("build", "run"))
