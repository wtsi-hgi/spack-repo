# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYieldcurve(RPackage):
	"""Modelling and Estimation of the Yield Curve

	Modelling the yield curve with some parametric models.
        The models implemented are: 
		Nelson, C.R., and A.F. Siegel (1987) <doi: 10.1086/296409>, 
		Diebold, F.X. and Li, C. (2006) <doi: 10.1016/j.jeconom.2005.03.005> 
		and Svensson, L.E. (1994) <doi: 10.3386/w4871>. 
		The package also includes the data of the term structure of interest rate of Federal Reserve Bank and European Central Bank.
	"""
	
	cran = "YieldCurve" 

	version("5.1", md5="647f13bc6b36a740aa235faa08db70ba")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
