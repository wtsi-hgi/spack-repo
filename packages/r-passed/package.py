# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPassed(RPackage):
	"""Calculate Power and Sample Size for Two Sample Mean Tests

	Power calculations are a critical component of any research study to determine the 
	minimum sample size necessary to detect differences between multiple groups. Here we 
	present an 'R' package, 'PASSED', that performs power and sample size calculations for 
	the test of two-sample means or ratios with data following beta, 
	gamma (Chang et al. (2011), <doi:10.1007/s00180-010-0209-1>), normal, 
	Poisson (Gu et al. (2008), <doi:10.1002/bimj.200710403>), binomial, geometric, and 
	negative binomial (Zhu and Lakkis (2014), <doi:10.1002/sim.5947>) distributions.
	"""
	
	cran = "PASSED" 

	version("1.2-2", md5="57b7fa47b3826331dd474d69657359e5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-betareg", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
