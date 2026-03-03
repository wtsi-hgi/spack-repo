# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClr(RPackage):
	"""Curve Linear Regression via Dimension Reduction

	A new methodology for linear regression with both curve response 
    and curve regressors, which is described in Cho, Goude, Brossat and Yao 
    (2013) <doi:10.1080/01621459.2012.722900> and (2015) 
    <doi:10.1007/978-3-319-18732-7_3>. The key idea behind this methodology is 
    dimension reduction based on a singular value decomposition in a Hilbert 
    space, which reduces the curve regression problem to several scalar linear 
    regression problems. 
	"""
	
	cran = "clr" 

	version("0.1.2", md5="c5f3f9a87279177fae66258da7ca45cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
