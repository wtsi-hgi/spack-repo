# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirtjml(RPackage):
	"""Joint Maximum Likelihood Estimation for High-Dimensional Item
Factor Analysis

	Provides constrained joint maximum likelihood estimation
    algorithms for item factor analysis (IFA) based on multidimensional item response theory
    models. So far, we provide functions for exploratory and confirmatory IFA based on the 
    multidimensional two parameter logistic (M2PL) model for binary response data. Comparing 
    with traditional estimation methods for IFA, the methods implemented in this package scale
    better to data with large numbers of respondents, items, and latent factors. The computation
    is facilitated by multiprocessing 'OpenMP' API. For more information, please refer to:
    1. Chen, Y., Li, X., & Zhang, S. (2018). Joint Maximum Likelihood Estimation for 
    High-Dimensional Exploratory Item Factor Analysis. Psychometrika, 1-23. 
    <doi:10.1007/s11336-018-9646-5>;
    2. Chen, Y., Li, X., & Zhang, S. (2019). Structured Latent Factor Analysis for Large-scale Data: 
    Identifiability, Estimability, and Their Implications. Journal of the American Statistical 
    Association, <doi: 10.1080/01621459.2019.1635485>.
	"""
	
	homepage = "https://github.com/slzhang-fd/mirtjml"
	cran = "mirtjml" 

	version("1.4.0", md5="b8080cc1fdbe3d92ec7bde1b8637423f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-gparotation", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
