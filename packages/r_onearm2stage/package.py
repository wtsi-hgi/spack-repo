# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnearm2stage(RPackage):
	"""Phase II Single-Arm Two-Stage Designs with Time-to-Event
Outcomes

	Two-stage design for single-arm phase II 
		trials with time-to-event endpoints (e.g., clinical trials on 
		immunotherapies among cancer patients) can be calculated using this package. 
		Two notable advantages of the package: 1) It provides flexible choices from 
		three design methods (optimal, minmax, and admissible), and 2) the power of
		the design is more accurately calculated using the exact variance in the
		one-sample log-rank test. The package can be used for 1) planning the sample
		sizes and other design parameters, and 2) conducting the interim and final
		analyses for the Go/No-go decisions. More details about the design method
		can be found in: Wu, J, Chen L, Wei J, Weiss H, Chauhan A. (2020).
		<doi:10.1002/pst.1983>.
	"""
	
	cran = "OneArm2stage" 

	version("1.2.1", md5="d30d72cf91539e9fbcbf2b6a6b23eac5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-ipdfromkm", type=("build", "run"))
