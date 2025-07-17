# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemminedrugs(RPackage):
    """DrugBank data set

    An annotation package for use with ChemmineR. This package includes data from DrugBank. DUD data can be downloaded using the "DUD()" function in ChemmineR.
    """

    bioc = "ChemmineDrugs"
    urls = [
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ChemmineDrugs_1.0.2.tar.gz",
        "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ChemmineDrugs/ChemmineDrugs_1.0.2.tar.gz",
    ]

    version(
        "1.0.2",
        sha256="c400d3a8b1c4cd4de3bf9d9ad751ccea90cd3a6b6c31a1327c95f9490d538750",
    )

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-chemminer", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-rsqlite", type=("build", "run"))
