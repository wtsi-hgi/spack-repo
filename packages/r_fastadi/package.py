# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastadi(RPackage):
	"""Self-Tuning Data Adaptive Matrix Imputation

	Implements the AdaptiveImpute matrix completion
    algorithm of 'Intelligent Initialization and Adaptive Thresholding for
    Iterative Matrix Completion',
    <https://amstat.tandfonline.com/doi/abs/10.1080/10618600.2018.1518238>.
    AdaptiveImpute is useful for embedding sparsely observed matrices,
    often out performs competing matrix completion algorithms, and
    self-tunes its hyperparameter, making usage easy.
	"""
	
	homepage = "https://github.com/RoheLab/fastadi"
	cran = "fastadi" 

	version("0.1.1", md5="b033345792c57da70855c921d4b9c644")

	depends_on("r-lrmf3", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ellipsis", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
