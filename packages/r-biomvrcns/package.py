# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiomvrcns(RPackage):
    """Copy Number study and Segmentation for multivariate biological data

    In this package, a Hidden Semi Markov Model (HSMM) and one homogeneous segmentation model are designed and implemented for segmentation genomic data, with the aim of assisting in transcripts detection using high throughput technology like RNA-seq or tiling array, and copy number analysis using aCGH or sequencing.
    """

    bioc = "biomvRCNS"

    version("1.48.0", commit="977442e0470cc33ec22f653f68ff5467466e51ac")
    version("1.42.2", commit="b3a0be77c391c71283515e38a9b822d11a0de40d")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-gviz", type=("build", "run"))
    depends_on("r-mvtnorm", type=("build", "run"))
