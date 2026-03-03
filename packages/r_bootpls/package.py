# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootpls(RPackage):
	"""Bootstrap Hyperparameter Selection for PLS Models and Extensions

	Several implementations of non-parametric stable bootstrap-based techniques to determine the numbers of components for Partial Least Squares linear or generalized linear regression models as well as and sparse Partial Least Squares linear or generalized linear regression models. The package collects techniques that were published in a book chapter (Magnanensi et al. 2016, 'The Multiple Facets of Partial Least Squares and Related Methods', <doi:10.1007/978-3-319-40643-5_18>) and two articles (Magnanensi et al. 2017, 'Statistics and Computing', <doi:10.1007/s11222-016-9651-4>) and (Magnanensi et al. 2021, 'Frontiers in Applied Mathematics and Statistics', accepted.).
	"""
	
	homepage = "https://fbertran.github.io/bootPLS/"
	cran = "bootPLS" 

	version("0.9.9", md5="a60b470d9a24b812370f8ea21657526d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-plsrglm", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-spls", type=("build", "run"))
	depends_on("r-bipartite", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
