# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLemur(RPackage):
    """Latent Embedding Multivariate Regression

    Fit a latent embedding multivariate regression (LEMUR) model to multi-condition single-cell data. The model provides a parametric description of single-cell data measured with complex experimental designs. The parametric model is used to (1) align conditions, (2) predict log fold changes between conditions for all cells, and (3) identify cell neighborhoods with consistent log fold changes. For those neighborhoods, a pseudobulked differential expression test is conducted to assess which genes are significantly changed.
    """

    homepage = "https://github.com/const-ae/lemur"
    bioc = "lemur"

    version("1.6.1", commit="126bb86b9a156002c05e7b367a15c77b1a10a114")
    version("1.0.5", commit="001ae9fc6bb6c79107f58553220b8e7e7c52f956")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-irlba", type=("build", "run"))
    depends_on("r-singlecellexperiment", type=("build", "run"))
    depends_on("r-summarizedexperiment", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-vctrs", type=("build", "run"))
    depends_on("r-glmgampoi@1.12:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-delayedmatrixstats", type=("build", "run"))
    depends_on("r-hdf5array", type=("build", "run"))
    depends_on("r-matrixgenerics", type=("build", "run"))
    depends_on("r-matrixstats", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-harmony", type=("build", "run"))
    depends_on("r-limma", type=("build", "run"))
    depends_on("r-biocneighbors", type=("build", "run"))
    depends_on("r-rcpparmadillo", type=("build", "run"))
