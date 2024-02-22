# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiglasso(RPackage):
	"""Extending Lasso Model Fitting to Big Data

	Extend lasso and elastic-net model fitting for ultra
    high-dimensional, multi-gigabyte data sets that cannot be loaded into
    memory. Designed to be more memory- and computation-efficient than existing
    lasso-fitting packages like 'glmnet' and 'ncvreg', thus allowing
    the user to analyze big data analysis even on an ordinary laptop.
	"""
	
	homepage = "https://yaohuizeng.github.io/biglasso/index.html"
	cran = "biglasso" 

	version("1.5.2", md5="f32a0155b5b0d1bcbda40ce58c9f1876")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-bigmemory", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8.600:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
