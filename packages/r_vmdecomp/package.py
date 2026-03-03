# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVmdecomp(RPackage):
	"""Variational Mode Decomposition

	'RcppArmadillo' implementation for the Matlab code of the 'Variational Mode Decomposition' and 'Two-Dimensional Variational Mode Decomposition'. For more information, see (i) 'Variational Mode Decomposition' by K. Dragomiretskiy and D. Zosso in IEEE Transactions on Signal Processing, vol. 62, no. 3, pp. 531-544, Feb.1, 2014, <doi:10.1109/TSP.2013.2288675>; (ii) 'Two-Dimensional Variational Mode Decomposition' by Dragomiretskiy, K., Zosso, D. (2015), In: Tai, XC., Bae, E., Chan, T.F., Lysaker, M. (eds) Energy Minimization Methods in Computer Vision and Pattern Recognition. EMMCVPR 2015. Lecture Notes in Computer Science, vol 8932. Springer, <doi:10.1007/978-3-319-14612-6_15>.
	"""
	
	homepage = "https://github.com/mlampros/VMDecomp"
	cran = "VMDecomp" 

	version("1.0.1", md5="94d5ca830fe7716760175b802845ea6e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
	depends_on("lapack", type=("build", "link", "run"))
	depends_on("blas", type=("build", "link", "run"))
	depends_on("arpack-ng", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
