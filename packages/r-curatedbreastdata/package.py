# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedbreastdata(RPackage):
    """Curated breast cancer gene expression data with survival and treatment information

    Curated human breast cancer tissue S4 ExpresionSet datasets from over 16 clinical trials comprising over 2,000 patients. All datasets contain at least one type of outcomes variable and treatment information (minimum level: whether they had chemotherapy and whether they had hormonal therapy). Includes code to post-process these datasets.
    """

    bioc = "curatedBreastData"

    version("2.36.0", commit="51e57331b309c4a8b05fd4608365a99434cfd1a1")
    version("2.30.0", commit="252ba232b853fb8b5fc214fd5f29637897ad6d97")

    depends_on("r@3:", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
