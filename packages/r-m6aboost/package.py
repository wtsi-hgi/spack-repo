# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RM6aboost(RPackage):
    """m6Aboost

    This package can help user to run the m6Aboost model on their own miCLIP2 data. The package includes functions to assign the read counts and get the features to run the m6Aboost model. The miCLIP2 data should be stored in a GRanges object. More details can be found in the vignette.
    """

    homepage = "https://github.com/ZarnackGroup/m6Aboost"
    bioc = "m6Aboost"

    version("1.14.0", commit="29c076f6b89d720e57031fd5b54a5f7227fa8694")
    version("1.8.0", commit="c64f738387585494b97adbd06e359c191b214e9f")

    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-adabag", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-experimenthub", type=("build", "run"))
