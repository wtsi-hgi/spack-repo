# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgvr(RPackage):
    """igvR: integrative genomics viewer

    Access to igv.js, the Integrative Genomics Viewer running in a web browser.
    """

    homepage = "https://gladkia.github.io/igvR/"
    bioc = "igvR"

    version("1.28.0", commit="94758605192ac0fe21b21d03503f5a31d0c471bc")
    version("1.22.0", commit="ace7a8934ba366cd5e5fc1d905cc1bc701891780")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-browserviz@2.17.1:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-httpuv", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
