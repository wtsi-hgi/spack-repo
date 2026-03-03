# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBmet(RPackage):
	"""Bayesian Multigroup Equivalence Testing

	Calculates the necessary quantities to perform Bayesian multigroup equivalence testing. 
             Currently the package includes the Bayesian models and equivalence criteria outlined in Pourmohamad and Lee (2023) 
             <doi:10.1002/sta4.645>, but more models and equivalence testing features may be added over time.
	"""
	
	cran = "bmet" 

	version("0.1.0", md5="43bf414e5b43c830b956b2331165716f")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
