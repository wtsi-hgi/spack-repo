# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToweranna(RPackage):
	"""A Method for Handling Missing Values in Prediction Applications

	Non-imputational method for handling missing values in 
   a prediction context, meaning that not only are there missing
   values in the training dataset, but also some values may be missing
   in future cases to be predicted. Based on the notion of regression
   averaging (Matloff (2017, ISBN: 9781498710916)).
	"""
	
	homepage = "https://github.com/matloff/toweranNA"
	cran = "toweranNA" 

	version("0.1.0", md5="bbc34a87c57970ef0a36973971e4734b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-regtools@0.8:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
