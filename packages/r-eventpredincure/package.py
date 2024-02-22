# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REventpredincure(RPackage):
	"""Event Prediction Including Cured Population

	Predicts enrollment and events assumed enrollment and treatment-specific time-to-event models, and calculates test statistics for time-to-event data with cured population based on the simulation.Methods for prediction event in the existence of cured population are as described in : Chen, Tai-Tsang(2016) <doi:10.1186/s12874-016-0117-3>. 
	"""
	
	cran = "EventPredInCure" 

	version("1.0", md5="b59986d1b8e0f8a8b08c6e09083dcf4e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-perm@1.0.0.2:", type=("build", "run"))
	depends_on("r-msm@1.7:", type=("build", "run"))
	depends_on("r-mlecens@0.1.7:", type=("build", "run"))
	depends_on("r-kmsurv@0.1.5:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-plotly@4.10.1:", type=("build", "run"))
	depends_on("r-survival@2.41.3:", type=("build", "run"))
	depends_on("r-matrix@1.2.14:", type=("build", "run"))
	depends_on("r-mvtnorm@1.1.3:", type=("build", "run"))
	depends_on("r-rstpm2@1.6.1:", type=("build", "run"))
	depends_on("r-numderiv@2016.8.1.1:", type=("build", "run"))
	depends_on("r-tmvtnsim@0.1.3:", type=("build", "run"))
	depends_on("r-erify@0.4:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-flexsurv@2.2.2:", type=("build", "run"))
	depends_on("r-mass@7.3.54:", type=("build", "run"))
