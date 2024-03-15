# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnclassify(RPackage):
	"""Learning Discrete Bayesian Network Classifiers from Data

	State-of-the art algorithms for learning discrete Bayesian network classifiers from data, including a number of those described in Bielza & Larranaga (2014) <doi:10.1145/2576868>, with functions for prediction, model evaluation and inspection.
	"""
	
	homepage = "https://github.com/bmihaljevic/bnclassify"
	cran = "bnclassify" 

	version("0.4.8", md5="dc9388838bb6e2ac64e10ca6cdeb1ed9")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-entropy@1.2:", type=("build", "run"))
	depends_on("r-matrixstats@0.14:", type=("build", "run"))
	depends_on("r-rpart@4.1.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
