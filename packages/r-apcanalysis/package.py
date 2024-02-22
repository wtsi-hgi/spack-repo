# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RApcanalysis(RPackage):
	"""Analysis of Unreplicated Orthogonal Experiments using All
Possible Comparisons

	Analysis of  data from unreplicated orthogonal experiments such as 2-level factorial and fractional factorial designs and Plackett-Burman designs using the all possible comparisons (APC) methodology developed by Miller (2005) <doi:10.1198/004017004000000608>.
	"""
	
	cran = "APCanalysis" 

	version("1.0", md5="1cd35855208e8d359b146304c5d36051")

	depends_on("r@3.3:", type=("build", "run"))
