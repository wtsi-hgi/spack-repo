# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlrintermbo(RPackage):
	"""Model-Based Optimization for 'mlr3' Through 'mlrMBO'

	The 'mlrMBO' package can ordinarily not be used for optimization within 'mlr3', because of
  incompatibilities of their respective class systems. 'mlrintermbo' offers a compatibility
  interface that provides 'mlrMBO' as an 'mlr3tuning' 'Tuner' object, for tuning of machine
  learning algorithms within 'mlr3', as well as a 'bbotk' 'Optimizer' object for optimization
  of general objective functions using the 'bbotk' black box optimization framework. The
  control parameters of 'mlrMBO' are faithfully reproduced as a 'paradox' 'ParamSet'.
	"""
	
	homepage = "https://github.com/mb706/mlrintermbo"
	cran = "mlrintermbo" 

	version("0.5.0", md5="f7e2a70ceb076c3e77563db17836eb8c")

	depends_on("r-backports", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-mlr3misc@0.1.4:", type=("build", "run"))
	depends_on("r-paradox", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-bbotk", type=("build", "run"))
	depends_on("r-mlr3tuning", type=("build", "run"))
