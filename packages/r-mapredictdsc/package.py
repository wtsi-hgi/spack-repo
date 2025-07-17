# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapredictdsc(RPackage):
    """Phenotype prediction using microarray data: approach of the best overall team in the IMPROVER Diagnostic Signature Challenge

    This package implements the classification pipeline of the best overall team (Team221) in the IMPROVER Diagnostic Signature Challenge. Additional functionality is added to compare 27 combinations of data preprocessing, feature selection and classifier types.
    """

    homepage = "http://bioinformaticsprb.med.wayne.edu/maPredictDSC"
    bioc = "maPredictDSC"

    version("1.46.0", commit="61c8eb1d2f965326c46a4fb86a2da85e4d2c0417")
    version("1.40.0", commit="20ea6c692d4cc2b6a1edb79a981e4a1edb2d860f")

    depends_on("r@2.15:", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-gcrma", type=("build", "run"))
    depends_on("r-roc", type=("build", "run"))
    depends_on("r-class", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))
    depends_on("r-caret", type=("build", "run"))
    depends_on("r-hgu133plus2-db", type=("build", "run"))
    depends_on("r-rocr", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-lungcanceracvssccgeo", type=("build", "run"))
