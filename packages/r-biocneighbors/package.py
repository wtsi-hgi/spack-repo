# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocneighbors(RPackage):
    """Nearest Neighbor Detection for Bioconductor Packages.

    Implements exact and approximate methods for nearest neighbor detection,
    in a framework that allows them to be easily switched within
    Bioconductor packages or workflows. Exact searches can be performed
    using the k-means for k-nearest neighbors algorithm or with vantage
    point trees. Approximate searches can be performed using the Annoy or
    HNSW libraries. Searching on either Euclidean or Manhattan distances is
    supported. Parallelization is achieved for all methods by using
    BiocParallel. Functions are also provided to search for all neighbors
    within a given distance."""

    bioc = "BiocNeighbors"
    git = "https://git.bioconductor.org/packages/BiocNeighbors"

    version("2.4.0", sha256="7367c7f5ca7c58a3f5b610b3babae2c31f3f310cfde349067da48897494fa0fb", url=["https://www.bioconductor.org/packages/3.22/bioc/src/contrib/BiocNeighbors_2.4.0.tar.gz", "https://www.bioconductor.org/packages/3.22/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_2.4.0.tar.gz"])
    version("1.8.2", commit="889bc91f8cb45d210b47ae5c0b9cfb86fb071ca2", url=["https://www.bioconductor.org/packages/3.12/bioc/src/contrib/BiocNeighbors_1.8.2.tar.gz", "https://www.bioconductor.org/packages/3.12/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.8.2.tar.gz"])
    version("2.2.0", url=["https://www.bioconductor.org/packages/3.21/bioc/src/contrib/BiocNeighbors_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.21/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_2.2.0.tar.gz"])
    version("1.20.2", md5="60f1ea60fb00cfd92dfa247765da9204", url=["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BiocNeighbors_1.20.2.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.20.2.tar.gz"])
    version("1.2.0", commit="f754c6300f835142536a4594ddf750481e0fe273", url=["https://www.bioconductor.org/packages/3.9/bioc/src/contrib/BiocNeighbors_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.9/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.2.0.tar.gz"])
    version("1.18.0", commit="4b19ef2a76baa0b001c426bad540ab9295bec78e", url=["https://www.bioconductor.org/packages/3.17/bioc/src/contrib/BiocNeighbors_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.17/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.18.0.tar.gz"])
    version("1.16.0", commit="3b227beead424314aab5ef847222f8f4243c684f", url=["https://www.bioconductor.org/packages/3.16/bioc/src/contrib/BiocNeighbors_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.16/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.16.0.tar.gz"])
    version("1.14.0", commit="670a1bd4d82636d28fbff50cea2157e16bb1a858", url=["https://www.bioconductor.org/packages/3.15/bioc/src/contrib/BiocNeighbors_1.14.0.tar.gz", "https://www.bioconductor.org/packages/3.15/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.14.0.tar.gz"])
    version("1.12.0", commit="3c8a290f75adc944b408e6e77a36f3a0c1509c4c", url=["https://www.bioconductor.org/packages/3.14/bioc/src/contrib/BiocNeighbors_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.14/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.12.0.tar.gz"])
    version("1.0.0", commit="e252fc04b6d22097f2c5f74406e77d85e7060770", url=["https://www.bioconductor.org/packages/3.8/bioc/src/contrib/BiocNeighbors_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.8/bioc/src/contrib/Archive/BiocNeighbors/BiocNeighbors_1.0.0.tar.gz"])

    depends_on("r@4.4:", type=("build", "run"), when="@2.4.0:")
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-assorthead@1.3.10:", type=("build", "run"), when="@2.4.0:")
    depends_on("r-assorthead", type=("build", "run"), when="@2.2.0:2.3")

    # Dependencies for versions 2.2 and lower
    depends_on("r-s4vectors", type=("build", "run"), when="@:2.2")
    depends_on("r-matrix", type=("build", "run"), when="@:2.2")
    depends_on("r-rcpphnsw", type=("build", "run"), when="@:2.2")
