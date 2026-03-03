# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsarima(RPackage):
	"""Two Functions for Generalized SARIMA Time Series Simulation

	Write SARIMA models in (finite) AR representation and simulate 
	generalized multiplicative seasonal autoregressive moving average (time) series 
	with Normal / Gaussian, Poisson or negative binomial distribution. 
	The methodology of this method is described in Briet OJT, Amerasinghe PH, and 
	Vounatsou P (2013) <doi:10.1371/journal.pone.0065761>.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "gsarima" 

	version("0.1-5", md5="98c79204118ec3942821dae47fde7710")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
