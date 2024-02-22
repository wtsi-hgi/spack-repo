# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REtasflp(RPackage):
	"""Mixed FLP and ML Estimation of ETAS Space-Time Point Processes
for Earthquake Description

	Estimation of the components of an ETAS (Epidemic Type Aftershock Sequence) model for earthquake description. Non-parametric background seismicity can be estimated through FLP (Forward Likelihood Predictive). New version 2.0.0: covariates have been introduced to explain the effects of external factors on the induced seismicity; the parametrization has been changed; Chiodi, Adelfio (2017)<doi:10.18637/jss.v076.i03>.
	"""
	
	cran = "etasFLP" 

	version("2.2.2", md5="7e0a57b38e2a9a56b9fc00799d7b04a4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mapdata", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
