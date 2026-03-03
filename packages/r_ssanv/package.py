# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsanv(RPackage):
	"""Sample Size Adjusted for Nonadherence or Variability of Input
Parameters

	A set of functions to calculate sample size for two-sample difference in means tests. Does adjustments for either nonadherence or variability that comes from using data to estimate parameters.
	"""
	
	cran = "ssanv" 

	version("1.1", md5="b31deb0e2ab0dbbf8ed512eb148126ef")

	depends_on("r@2.1.1:", type=("build", "run"))
