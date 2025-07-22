# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAucell(RPackage):
    """AUCell: Analysis of 'gene set' activity in single-cell RNA-seq data (e.g. identify cells with specific gene signatures)

    AUCell allows to identify cells with active gene sets (e.g. signatures, gene modules...) in single-cell RNA-seq data. AUCell uses the "Area Under the Curve" (AUC) to calculate whether a critical subset of the input gene set is enriched within the expressed genes for each cell. The distribution of AUC scores across all the cells allows exploring the relative expression of the signature. Since the scoring method is ranking-based, AUCell is independent of the gene expression units and the normalization procedure. In addition, since the cells are evaluated individually, it can easily be applied to bigger datasets, subsetting the expression matrix if needed.
    """

    homepage = "http://scenic.aertslab.org"
    bioc = "AUCell"

    version("1.30.1", commit="3094f3be3851730528560acae29d9d70297ca5b3")
    version("1.24.0", commit="8c22389d634c31bb2ee797ef572de80efbd3a0d3")

    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-gseabase", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-mixtools", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
