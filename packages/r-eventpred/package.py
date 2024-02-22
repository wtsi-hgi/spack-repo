# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventpred(RPackage):
	"""Event Prediction

	Predicts enrollment and events at the design or analysis stage using specified enrollment and time-to-event models through simulations.
	"""
	
	homepage = "https://github.com/kaifenglu/eventPred"
	cran = "eventPred" 

	version("0.2.4", md5="f41c8772299fae0e3a524f0b1f4c5c64")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-plotly@4.10.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.14:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-rstpm2@1.6.1:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-purrr@1.0.2:", type=("build", "run"))
	depends_on("r-flexsurv@2.2.2:", type=("build", "run"))
	depends_on("r-erify@0.4:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
