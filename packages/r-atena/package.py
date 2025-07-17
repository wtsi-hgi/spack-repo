# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAtena(RPackage):
    """Analysis of Transposable Elements

    Quantify expression of transposable elements (TEs) from RNA-seq data through different methods, including ERVmap, TEtranscripts and Telescope. A common interface is provided to use each of these methods, which consists of building a parameter object, calling the quantification function with this object and getting a SummarizedExperiment object as output container of the quantified expression profiles. The implementation allows one to quantify TEs and gene transcripts in an integrated manner.
    """

    homepage = "https://github.com/functionalgenomics/atena"
    bioc = "atena"

    version("1.14.1", commit="9b1f68fc3ef67b8860439f4ffd3a06fae42eb3c5")
    version("1.8.0", commit="634a46974205fe83e7e83c1d6900ae070efd71fc")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-biocparallel", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("r-rsamtools", type=("build", "run"))
    depends_on("r-genomeinfodb", type=("build", "run"))
    depends_on("r-squarem", type=("build", "run"))
    depends_on("r-sparsematrixstats", type=("build", "run"))
    depends_on("r-annotationhub", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
