# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdimpute(RPackage):
    """Adaptive Dropout Imputer (ADImpute)

    Single-cell RNA sequencing (scRNA-seq) methods are typically unable to quantify the expression levels of all genes in a cell, creating a need for the computational prediction of missing values (‘dropout imputation’). Most existing dropout imputation methods are limited in the sense that they exclusively use the scRNA-seq dataset at hand and do not exploit external gene-gene relationship information. Here we propose two novel methods: a gene regulatory network-based approach using gene-gene relationships learnt from external data and a baseline approach corresponding to a sample-wide average. ADImpute can implement these novel methods and also combine them with existing imputation methods (currently supported: DrImpute, SAVER). ADImpute can learn the best performing method per gene and combine the results from different methods into an ensemble.
    """

    bioc = "ADImpute"

    version("1.18.0", commit="e66afe6c2bd2c7992a70b09369c436c5e3574da6")
    version("1.12.0", commit="327d96df8c63e88766424ec115c730cdae449a3f")

    depends_on("r@4:", type=("build", "run"))
    depends_on("r-checkmate", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-drimpute", type=("build", "run"))
    depends_on("r-kernlab", type=("build", "run"))
    depends_on("r-mass", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-rsvd", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-saver", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
