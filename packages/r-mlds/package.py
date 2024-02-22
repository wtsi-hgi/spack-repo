# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlds(RPackage):
	"""Maximum Likelihood Difference Scaling

	Difference scaling is a method for scaling perceived 
  supra-threshold differences.  The package contains functions that
  allow the user to design and run a difference scaling experiment, 
  to fit the resulting data by maximum likelihood and test the
  internal validity of the estimated scale.
	"""
	
	cran = "MLDS" 

	version("0.5.1", md5="51135485848c460596e9f5278a75ccad")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
