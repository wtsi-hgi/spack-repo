# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXnastring(RPackage):
    """Efficient Manipulation of Modified Oligonucleotide Sequences

    The XNAString package allows for description of base sequences and associated chemical modifications in a single object. XNAString is able to capture single stranded, as well as double stranded molecules. Chemical modifications are represented as independent strings associated with different features of the molecules (base sequence, sugar sequence, backbone sequence, modifications) and can be read or written to a HELM notation. It also enables secondary structure prediction using RNAfold from ViennaRNA. XNAString is designed to be efficient representation of nucleic-acid based therapeutics, therefore it stores information about target sequences and provides interface for matching and alignment functions from Biostrings package.
    """

    bioc = "XNAString"

    version("1.16.0", commit="d1ff0c238396b0844deafa5a300f15c8f98bf75d")
    version("1.10.0", commit="2237ef835e1a4a305e79d5d5b2fe93328b49d199")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-bsgenome", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-stringi", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-future-apply", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-formattable", type=("build", "run"))
    # Added: XNAString imports/uses pwalign (Bioconductor)
    depends_on("r-pwalign", type=("build", "run"))
