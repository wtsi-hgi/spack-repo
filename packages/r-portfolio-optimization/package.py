# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPortfolioOptimization(RPackage):
	"""Contemporary Portfolio Optimization

	Simplify your portfolio optimization process by applying a contemporary modeling way to model and solve your portfolio problems. While most approaches and packages are rather complicated this one tries to simplify things and is agnostic regarding risk measures as well as optimization solvers. Some of the methods implemented are described by Konno and Yamazaki (1991) <doi:10.1287/mnsc.37.5.519>, Rockafellar and Uryasev (2001) <doi:10.21314/JOR.2000.038> and Markowitz (1952) <doi:10.1111/j.1540-6261.1952.tb01525.x>.
	"""
	
	homepage = "http://www.finance-r.com/"
	cran = "portfolio.optimization" 

	version("1.0-0", md5="71d0751079c3481a78b91a1798e69ae5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-modopt-matlab", type=("build", "run"))
