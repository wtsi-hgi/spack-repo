# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVarianttoolsdata(RPackage):
    """Data for the VariantTools tutorial

    Data from the sequencing of a 50/50 mixture of HapMap trio samples NA12878 (CEU) and NA19240 (YRI), subset to the TP53 region.
    """

    bioc = "VariantToolsData"

    version("1.32.0", commit="a339056add002a92800aee39509fd37c3551f40a")
    version("1.26.0", commit="946f7310e616c2ffa84001a44b7cbbec6e06d202")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-variantannotation@1.7.35:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
