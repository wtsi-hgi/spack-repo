# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchelor(RPackage):
    """Single-Cell Batch Correction Methods.

    Implements a variety of methods for batch correction of single-cell (RNA
    sequencing) data. This includes methods based on detecting mutually nearest
    neighbors, as well as several efficient variants of linear regression of
    the log-expression values. Functions are also provided to perform global
    rescaling to remove differences in depth between batches, and to perform a
    principal components analysis that is robust to differences in the numbers
    of cells across batches."""

    bioc = "batchelor"

    version("1.14.1", commit="a1f3e84b3a2c1fe3d0433c01a69090175ddc624a")

    depends_on ("r-singlecellexperiment", type=("build", "run"))
    depends_on ("r-summarizedexperiment", type=("build", "run"))
    depends_on ("r-s4vectors", type=("build", "run"))
    depends_on ("r-biocgenerics", type=("build", "run"))
    depends_on ("r-rcpp", type=("build", "run"))
    depends_on ("r-igraph", type=("build", "run"))
    depends_on ("r-biocneighbors", type=("build", "run"))
    depends_on ("r-biocsingular", type=("build", "run"))
    depends_on ("r-matrix", type=("build", "run"))
    depends_on ("r-delayedarray", type=("build", "run"))
    depends_on ("r-delayedmatrixstats", type=("build", "run"))
    depends_on ("r-biocparallel", type=("build", "run"))
    depends_on ("r-scuttle", type=("build", "run"))
    depends_on ("r-residualmatrix", type=("build", "run"))
    depends_on ("r-scaledmatrix", type=("build", "run"))
    depends_on ("r-beachmat", type=("build", "run"))
