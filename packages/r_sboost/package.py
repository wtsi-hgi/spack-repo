# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSboost(RPackage):
	"""Machine Learning with AdaBoost on Decision Stumps

	Creates classifier for binary outcomes using Adaptive Boosting 
    (AdaBoost) algorithm on decision stumps with a fast C++ implementation. 
    For a description of AdaBoost, see Freund and Schapire (1997) 
    <doi:10.1006/jcss.1997.1504>. This type of classifier is nonlinear, but
    easy to interpret and visualize. Feature vectors may be a combination of
    continuous (numeric) and categorical (string, factor) elements. Methods 
    for classifier assessment, predictions, and cross-validation also included.
	"""
	
	homepage = "https://github.com/jadonwagstaff/sboost"
	cran = "sboost" 

	version("0.1.2", md5="5eb4b23a75ad06b92cbabe95a8828954")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-rlang@0.2.1:", type=("build", "run"))
	depends_on("r-rcpp@0.12.17:", type=("build", "run"))
