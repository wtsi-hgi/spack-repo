# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbnlearn(RPackage):
	"""Dynamic Bayesian Network Structure Learning, Parameter Learning
and Forecasting

	It allows to learn the structure of univariate time series, learning parameters and forecasting. 
             Implements a model of Dynamic Bayesian Networks with temporal windows, 
             with collections of linear regressors for Gaussian nodes, 
             based on the introductory texts of Korb and Nicholson (2010) <doi:10.1201/b10391> and 
             Nagarajan, Scutari and Lèbre (2013) <doi:10.1007/978-1-4614-6446-4>.
	"""
	
	cran = "dbnlearn" 

	version("0.1.0", md5="680e9aeca143929543918a716770c178")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-bnviewer", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
