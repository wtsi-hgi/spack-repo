# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandom(RPackage):
	"""True Random Numbers using RANDOM.ORG

	The true random number service provided by the RANDOM.ORG
 website created by Mads Haahr samples atmospheric noise via radio tuned to
 an unused broadcasting frequency together with a skew correction algorithm
 due to John von Neumann.  More background is available in the included
 vignette based on an essay by Mads Haahr.  In its current form, the package
 offers functions to retrieve random integers, randomized sequences and
 random strings.
	"""
	
	homepage = "https://www.random.org"
	cran = "random" 

	version("0.2.6", md5="0a642b1f4cd45f9eaa2ed34aa3f7df90")

	depends_on("r@2.8:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
