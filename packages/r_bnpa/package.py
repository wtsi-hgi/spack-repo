# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnpa(RPackage):
	"""Bayesian Networks & Path Analysis

	This project aims to enable the method of Path Analysis to infer causalities 
             from data. For this we propose a hybrid approach, which uses Bayesian network 
             structure learning algorithms from data to create the input file for creation of a 
             PA model. The process is performed in a semi-automatic way by our intermediate 
             algorithm, allowing novice researchers to create and evaluate their own PA models
             from a data set. The references used for this project are: 
             Koller, D., & Friedman, N. (2009). Probabilistic graphical models: principles and techniques. MIT press. <doi:10.1017/S0269888910000275>. 
             Nagarajan, R., Scutari, M., & Lèbre, S. (2013). Bayesian networks in r. Springer, 122, 125-127. Scutari, M., & Denis, J. B. <doi:10.1007/978-1-4614-6446-4>.
             Scutari M (2010). Bayesian networks: with examples in R. Chapman and Hall/CRC. <doi:10.1201/b17065>. 
             Rosseel, Y. (2012). lavaan: An R Package for Structural Equation Modeling. Journal of Statistical Software, 48(2), 1 - 36. <doi:10.18637/jss.v048.i02>.
	"""
	
	homepage = "https://sites.google.com/site/bnparp/."
	cran = "bnpa" 

	version("0.3.0", md5="431dac95f6947ab3d0b5086872f1277a")

	depends_on("r-bnlearn", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-lavaan", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-semplot", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
