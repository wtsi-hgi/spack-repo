# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScarray(RPackage):
    """Large-scale single-cell RNA-seq data manipulation with GDS files

    Provides large-scale single-cell RNA-seq data manipulation using Genomic Data Structure (GDS) files. It combines dense and sparse matrices stored in GDS files and the Bioconductor infrastructure framework (SingleCellExperiment and DelayedArray) to provide out-of-memory data storage and large-scale manipulation using the R programming language.
    """

    homepage = "https://github.com/AbbVie-ComputationalGenomics/SCArray"
    bioc = "SCArray"

    version("1.16.0", commit="2581ee7f5f1c9f3bddf9c2ce871bdc73dcc03e2e")
    version("1.10.0", commit="076182529d37e365f90fc561e79e975438994680")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-gdsfmt@1.36:", type=("build", "run"))
    depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
