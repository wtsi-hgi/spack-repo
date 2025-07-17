# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiscuiteer(RPackage):
    """Convenience Functions for Biscuit

    A test harness for bsseq loading of Biscuit output, summarization of WGBS data over defined regions and in mappable samples, with or without imputation, dropping of mostly-NA rows, age estimates, etc.
    """

    homepage = "https://github.com/trichelab/biscuiteer"
    bioc = "biscuiteer"

    version("1.22.0", commit="44c7542f20e2f94986c5692d0e04a69eea578d1c")
    version("1.16.0", commit="ebfa0bfe511eb9c176c1c99d8c515228ec9da8e4")

    depends_on("r@4.1:", type=("build", "run"))
    depends_on("r-biscuiteerdata", type=("build", "run"))
    depends_on("r-bsseq", type=("build", "run"))
    depends_on("r-readr", type=("build", "run"))
    depends_on("r-qualv", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-impute", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-variantannotation", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-mus-musculus", type=("build", "run"))
    depends_on("r-homo-sapiens", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rtracklayer", type=("build", "run"))
    depends_on("r-qdnaseq", type=("build", "run"))
    depends_on("r-dmrseq", type=("build", "run"))
    depends_on("r-r-utils", type=("build", "run"))
    depends_on("r-gtools", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
