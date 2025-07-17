# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScatacExplorer(RPackage):
    """A Collection of Single-cell ATAC Sequencing Datasets and Corresponding Metadata

    This package provides a tool to search and download a collection of publicly available single cell ATAC-seq datasets and their metadata. scATAC-Explorer aims to act as a single point of entry for users looking to study single cell ATAC-seq data. Users can quickly search available datasets using the metadata table and download datasets of interest for immediate analysis within R.
    """

    bioc = "scATAC.Explorer"

    version("1.14.0", commit="0812e0aba6126b4a446072afd1796b1703557426")
    version("1.8.0", commit="133348d7a5c6c6c9b75e4b4f3e5ca0856dbff27c")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
