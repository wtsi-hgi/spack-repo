# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSccb2(RPackage):
    """CB2 improves power of cell detection in droplet-based single-cell RNA sequencing data

    scCB2 is an R package implementing CB2 for distinguishing real cells from empty droplets in droplet-based single cell RNA-seq experiments (especially for 10x Chromium). It is based on clustering similar barcodes and calculating Monte-Carlo p-value for each cluster to test against background distribution. This cluster-level test outperforms single-barcode-level tests in dealing with low count barcodes and homogeneous sequencing library, while keeping FDR well controlled.
    """

    homepage = "https://github.com/zijianni/scCB2"
    bioc = "scCB2"

    version("1.18.0", commit="343e582cfd076d68c597080cd7599fe9f1050dae")
    version("1.12.0", commit="bf81d7752bf242066c5ac6f2acabd68c6c364941")

    depends_on("r@3.6:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-edger", type=("build", "run"))
    depends_on("r-rhdf5", type=("build", "run"))
    depends_on("r-dropletutils", type=("build", "run"))
    depends_on("r-doparallel", type=("build", "run"))
    depends_on("r-iterators", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))
