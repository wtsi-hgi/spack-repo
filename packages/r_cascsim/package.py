# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCascsim(RPackage):
	"""Casualty Actuarial Society Individual Claim Simulator

	It is an open source insurance claim simulation engine sponsored
    by the Casualty Actuarial Society. It generates individual insurance claims 
	including open claims, reopened claims, incurred but not reported claims 
	and future claims. It also includes claim data fitting functions to help set 
	simulation assumptions. It is useful for claim level reserving analysis.
	Parodi (2013) <https://www.actuaries.org.uk/documents/triangle-free-reserving-non-traditional-framework-estimating-reserves-and-reserve-uncertainty>.
	"""
	
	cran = "cascsim" 

	version("0.4", md5="c66a0b7c1786158e26020a9cd7ff6b69")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-r2html", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
