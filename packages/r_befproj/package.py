# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBefproj(RPackage):
	"""Makes a Local Population Projection

	This is a sub national population projection model for calculating
    population development. The model uses a cohort component method.
    Further reading: Stanley K. Smith: A Practitioner's Guide to State and 
    Local Population Projections. 2013.  <doi:10.1007/978-94-007-7551-0>. 
	"""
	
	cran = "befproj" 

	version("0.1.1", md5="d94a33689ee9bb00d884be51e9209991")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
