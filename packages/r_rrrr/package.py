# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrrr(RPackage):
	"""Online Robust Reduced-Rank Regression Estimation

	Methods for estimating online robust reduced-rank regression. 
    The Gaussian maximum likelihood estimation method is described in Johansen, S. (1991) <doi:10.2307/2938278>.
    The majorisation-minimisation estimation method is partly described in Zhao, Z., & Palomar, D. P. (2017) <doi:10.1109/GlobalSIP.2017.8309093>.
    The description of the generic stochastic successive upper-bound minimisation method
    and the sample average approximation can be found in Razaviyayn, M., Sanjabi, M., & Luo, Z. Q. (2016) <doi:10.1007/s10107-016-1021-7>.
	"""
	
	homepage = "https://pkg.yangzhuoranyang.com/RRRR/"
	cran = "RRRR" 

	version("1.1.1", md5="faece7258dbd52bf1f52f12fb49e029a")

	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
