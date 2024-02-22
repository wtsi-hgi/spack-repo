# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGslnls(RPackage):
	"""GSL Nonlinear Least-Squares Fitting

	An R interface to nonlinear least-squares optimization with the GNU Scientific Library (GSL), see M. Galassi et al. (2009, ISBN:0954612078). The available trust region methods include the Levenberg-Marquardt algorithm with and without geodesic acceleration, the Steihaug-Toint conjugate gradient algorithm for large systems and several variants of Powell's dogleg algorithm. The interface includes multi-start optimization using quasi-random samples based on a modified version of algorithm in Hickernell and Yuan (1997, OR Transactions). Bindings are provided to tune a number of parameters affecting the low-level aspects of the trust region algorithms. The interface mimics R's nls() function and returns model objects inheriting from the same class.
	"""
	
	homepage = "https://github.com/JorisChau/gslnls"
	cran = "gslnls" 

	version("1.2.0", md5="8e4b24e9c6e136e348aaf8bb9a7b84d8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("gsl@2.2:", type=("build", "link", "run"))
