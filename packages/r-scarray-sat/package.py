# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScarraySat(RPackage):
    """Large-scale single-cell RNA-seq data analysis using GDS files and Seurat

    Extends the Seurat classes and functions to support Genomic Data Structure (GDS) files as a DelayedArray backend for data representation. It relies on the implementation of GDS-based DelayedMatrix in the SCArray package to represent single cell RNA-seq data. The common optimized algorithms leveraging GDS-based and single cell-specific DelayedMatrix (SC_GDSMatrix) are implemented in the SCArray package. SCArray.sat introduces a new SCArrayAssay class (derived from the Seurat Assay), which wraps raw counts, normalized expressions and scaled data matrix based on GDS-specific DelayedMatrix. It is designed to integrate seamlessly with the Seurat package to provide common data analysis in the SeuratObject-based workflow. Compared with Seurat, SCArray.sat significantly reduces the memory usage without downsampling and can be applied to very large datasets.
    """

    bioc = "SCArray.sat"

    version("1.8.0", commit="108b01c777705b4edd810fb49116f272175b7a86")
    version("1.2.1", commit="9bfe743a81839cff08f0010fc8a71e1123e250a7")

    depends_on("r-scarray@1.7.13:", type=("build", "run"))
    depends_on("r-seuratobject@4:", type=("build", "run"))
    depends_on("r-seurat@4:", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-gdsfmt", type=("build", "run"))
    depends_on("r-delayedarray", type=("build", "run"))
    depends_on("r-biocsingular", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
