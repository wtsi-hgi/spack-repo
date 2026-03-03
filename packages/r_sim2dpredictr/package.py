# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSim2dpredictr(RPackage):
	"""Simulate Outcomes Using Spatially Dependent Design Matrices

	Provides tools for simulating spatially dependent predictors (continuous or binary),
    which are used to generate scalar outcomes in a (generalized) linear model framework. Continuous
    predictors are generated using traditional multivariate normal distributions or Gauss Markov random
    fields with several correlation function approaches (e.g., see Rue (2001) <doi:10.1111/1467-9868.00288>
    and Furrer and Sain (2010) <doi:10.18637/jss.v036.i10>), while binary predictors are generated using
    a Boolean model (see Cressie and Wikle (2011, ISBN: 978-0-471-69274-4)). Parameter vectors 
	exhibiting spatial clustering can also be easily specified by the user.  
	"""
	
	homepage = "https://github.com/jmleach-bst/sim2Dpredictr"
	cran = "sim2Dpredictr" 

	version("0.1.1", md5="1688207dd0e2332ca5f7363f20a4132e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-spam@2.2.0:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
