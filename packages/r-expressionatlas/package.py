# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExpressionatlas(RPackage):
    """Download datasets from EMBL-EBI Expression Atlas

    This package is for searching for datasets in EMBL-EBI Expression Atlas, and downloading them into R for further analysis. Each Expression Atlas dataset is represented as a SimpleList object with one element per platform. Sequencing data is contained in a SummarizedExperiment object, while microarray data is contained in an ExpressionSet or MAList object.
    """

    bioc = "ExpressionAtlas"

    version("2.0.0", commit="ba47133d21353651cf7de3dd7526e8278cc94fed")
    version("1.30.0", commit="62d01eee1576fd093c5aeb52997523c8539ddf66")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-xml2", type=("build", "run"))
    depends_on("r-rcurl", type=("build", "run"))
    depends_on("r-jsonlite", type=("build", "run"))
    depends_on("r-biocstyle", type=("build", "run"))
    depends_on("r-xml", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
