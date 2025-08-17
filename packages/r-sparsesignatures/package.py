# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSparsesignatures(RPackage):
    """SparseSignatures

    Point mutations occurring in a genome can be divided into 96 categories based on the base being mutated, the base it is mutated into and its two flanking bases. Therefore, for any patient, it is possible to represent all the point mutations occurring in that patient's tumor as a vector of length 96, where each element represents the count of mutations for a given category in the patient. A mutational signature represents the pattern of mutations produced by a mutagen or mutagenic process inside the cell. Each signature can also be represented by a vector of length 96, where each element represents the probability that this particular mutagenic process generates a mutation of the 96 above mentioned categories. In this R package, we provide a set of functions to extract and visualize the mutational signatures that best explain the mutation counts of a large number of patients.
    """

    homepage = "https://github.com/danro9685/SparseSignatures"
    bioc = "SparseSignatures"

    version("2.18.0", commit="2e88f4acb4435b259ca5a18f06b0d945e8466deb")
    version("2.12.0", commit="761604b839f193991f49e8cd7ed95195428bcdf4")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-nmf", type=("build", "run"))
    depends_on("r-nnlasso", type=("build", "run"))
    depends_on("r-nnls", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-gridextra", type=("build", "run"))
    depends_on("r-reshape2", type=("build", "run"))
    # Missing runtime dependency required by SparseSignatures
    depends_on("r-rhpcblasctl", type=("build", "run"))
