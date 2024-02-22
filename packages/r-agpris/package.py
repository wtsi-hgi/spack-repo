# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgpris(RPackage):
	"""AGricultural PRoductivity in Space

	Functionalities to simulate space-time data and to estimate dynamic-spatial panel data models. 
             Estimators implemented are the BCML (Elhorst (2010), <doi:10.1016/j.regsciurbeco.2010.03.003>), the MML (Elhorst (2010) <doi:10.1016/j.regsciurbeco.2010.03.003>) and the INLA Bayesian estimator (Lindgren and Rue, (2015) <doi:10.18637/jss.v063.i19>; Bivand, Gomez-Rubio and Rue, (2015) <doi:10.18637/jss.v063.i20>) 
             adapted to panel data. The package contains functions to replicate the analyses of the scientific article entitled "Agricultural Productivity in Space" (Baldoni and Esposti (2021), <doi:10.1111/ajae.12155>)).
	"""
	
	cran = "AGPRIS" 

	version("2.0", md5="bcfa6fff31f444e2a207026e6e3e695e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
