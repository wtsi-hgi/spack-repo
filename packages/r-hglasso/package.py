# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHglasso(RPackage):
	"""Learning Graphical Models with Hubs

	Implements the hub graphical lasso and hub covariance graph proposal by Tan, KM., London, P., Mohan, K., Lee, S-I., Fazel, M., and Witten, D. (2014). Learning graphical models with hubs. Journal of Machine Learning Research 15(Oct):3297-3331.
	"""
	
	cran = "hglasso" 

	version("1.3", md5="867cbb5dc02dfd81fdc72256aba55278")

	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
