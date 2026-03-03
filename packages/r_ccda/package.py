# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcda(RPackage):
	"""Combined Cluster and Discriminant Analysis

	Implements the combined cluster and discriminant analysis method for finding homogeneous groups of data with known origin as described in Kovacs et. al (2014): Classification into homogeneous groups using combined cluster and discriminant analysis (CCDA). Environmental Modelling & Software. <doi:10.1016/j.envsoft.2014.01.010>.
	"""
	
	cran = "ccda" 

	version("1.1.1", md5="dc57da9bc49e000294d1c94ee4cf63ad")

	depends_on("r-mass", type=("build", "run"))
