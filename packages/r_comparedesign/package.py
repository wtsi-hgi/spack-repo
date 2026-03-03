# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComparedesign(RPackage):
	"""Statistical Functions for the Design of Studies with Composite
Endpoints

	It has been designed to calculate the required sample size in randomized clinical trials with composite endpoints. It also calculates the expected effect and the probability of observing the composite endpoint, among others. The methodology can be found in Bofill & Gómez (2019) <doi:10.1002/sim.8092> and Gómez & Lagakos (2013) <doi:10.1002/sim.5547>. 
	"""
	
	cran = "CompAREdesign" 

	version("2.3.1", md5="96e67239ce4d6094807ea6992c8fbcdd")

	depends_on("r-copula", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
