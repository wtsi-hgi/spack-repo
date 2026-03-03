# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRiemann(RPackage):
	"""Learning with Data on Riemannian Manifolds

	We provide a variety of algorithms for manifold-valued data, including Fréchet summaries, hypothesis testing, clustering, visualization, and other learning tasks. See Bhattacharya and Bhattacharya (2012) <doi:10.1017/CBO9781139094764> for general exposition to statistics on manifolds.
	"""
	
	homepage = "https://kisungyou.com/Riemann/"
	cran = "Riemann" 

	version("0.1.4", md5="f3457cc8d3f7aba5fc89470a7ddfa90e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-riembase", type=("build", "run"))
	depends_on("r-rdimtools", type=("build", "run"))
	depends_on("r-t4cluster", type=("build", "run"))
	depends_on("r-deoptim", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-maotai@0.2.2:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
