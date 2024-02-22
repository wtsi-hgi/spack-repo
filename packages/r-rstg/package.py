# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstg(RPackage):
	"""STG : Feature Selection using STochastic Gates

	'STG' is a method for feature selection in neural network. The procedure is based on probabilistic relaxation of the l0 norm of features, or the count of the number of selected features. The framework simultaneously learns either a nonlinear regression or classification function while selecting a small subset of features. Read more: Yamada et al. (2020) <https://proceedings.mlr.press/v119/yamada20a.html>.
	"""
	
	cran = "Rstg" 

	version("0.0.1", md5="54828b921dfc22148683ad09bd555f28")

	depends_on("r-reticulate@1.4:", type=("build", "run"))
