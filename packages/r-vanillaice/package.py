# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVanillaice(RPackage):
    """A Hidden Markov Model for high throughput genotyping arrays

    Hidden Markov Models for characterizing chromosomal alteration in high throughput SNP arrays.
    """

    bioc = "VanillaICE"

    version("1.70.1", commit="874022b76ff940dc6e1185d640b1d1ea6cb3e043")
    version("1.64.1", commit="ecd1e242bcd53654864863b6ecad8ca9e13cc3b6")
    version("1.64.0", md5="557131c410cc7474d15a4cc9a7d940de")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biocgenerics@0.13.6:", type=("build", "run"))
    depends_on("r-genomicranges@1.27.6:", type=("build", "run"))
    depends_on("r-summarizedexperiment@1.5.3:", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-s4vectors@0.23.18:", type=("build", "run"))
    depends_on("r-iranges@1.14:", type=("build", "run"))
    depends_on("r-oligoclasses@1.31.1:", type=("build", "run"))
    depends_on("r-foreach", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-genomeinfodb@1.11.4:", type=("build", "run"))
    depends_on("r-crlmm", type=("build", "run"))
    depends_on("r-bsgenome-hsapiens-ucsc-hg18", type=("build", "run"))
