# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVecctmvn(RPackage):
	"""Multivariate Normal Probabilities using Vecchia Approximation

	Under a different representation of the multivariate normal (MVN) probability, we can use the Vecchia approximation to sample the integrand at a linear complexity with respect to n. Additionally, both the SOV algorithm from Genz (92) and the exponential-tilting method from Botev (2017) can be adapted to linear complexity. The reference for the method implemented in this package is Jian Cao and Matthias Katzfuss (2024) "Linear-Cost Vecchia Approximation of Multivariate Normal Probabilities" <arXiv:2311.09426>. Two major references for the development of our method are Alan Genz (1992) "Numerical Computation of Multivariate Normal Probabilities" <doi:10.1080/10618600.1992.10477010> and Z. I. Botev (2017) "The Normal Law Under Linear Restrictions: Simulation and Estimation via Minimax Tilting" <arXiv:1603.04166>.
	"""
	
	cran = "VeccTMVN" 

	version("1.0.0", md5="1c615cbe26791333e8d0d1139076d3af")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix@1.5.3:", type=("build", "run"))
	depends_on("r-gpgp@0.4:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
	depends_on("r-gpvecchia", type=("build", "run"))
	depends_on("r-truncatednormal", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
