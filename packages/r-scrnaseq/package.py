# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrnaseq(RPackage):
    """Collection of Public Single-Cell RNA-Seq Datasets

    Gene-level counts for a collection of public scRNA-seq datasets, provided as SingleCellExperiment objects with cell- and gene-level metadata.
    """

    bioc = "scRNAseq"

    version("2.22.0", commit="62a2b70785fd41f290ba5fd2b52072cb2e33ebb3")
    version("2.16.0", commit="0bc6ab5602069dd57643d84d4536fba0426fbc65")

    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-experimenthub@2.3.4:", type=("build", "run"))
    depends_on("r-annotationhub@3.3.6:", type=("build", "run"))
    depends_on("r-annotationdbi", type=("build", "run"))
    depends_on("r-ensembldb", type=("build", "run"))
    depends_on("r-genomicfeatures", type=("build", "run"))
