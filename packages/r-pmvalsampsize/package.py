# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmvalsampsize(RPackage):
	"""Sample Size for External Validation of a Prediction Model

	Computes the minimum sample size required for the external validation of an existing multivariable prediction model using the criteria proposed by Archer (2020) <doi:10.1002/sim.8766> and Riley (2021) <doi:10.1002/sim.9025>.
	"""
	
	cran = "pmvalsampsize" 

	version("0.1.0", md5="99c2ed908c7afaab32696f9c9c5c9545")

	depends_on("r@2.1:", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
