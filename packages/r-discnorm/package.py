# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscnorm(RPackage):
	"""Test for Discretized Normality in Ordinal Data

	Tests whether multivariate ordinal data may stem from discretizing a multivariate normal distribution.
             The test is described by Foldnes and Grønneberg (2019) <doi:10.1080/10705511.2019.1673168>. 
             In addition, an adjusted polychoric correlation estimator is provided that takes marginal knowledge into account,
             as described by Grønneberg and Foldnes (2022) <doi:10.1037/met0000495>. 
	"""
	
	cran = "discnorm" 

	version("0.2.1", md5="a7c819b68498efddfc3e1307dea68020")

	depends_on("r-lavaan@0.6.10:", type=("build", "run"))
	depends_on("r-arules", type=("build", "run"))
	depends_on("r-sirt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-gofkernel", type=("build", "run"))
