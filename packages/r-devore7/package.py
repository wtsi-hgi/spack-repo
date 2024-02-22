# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDevore7(RPackage):
	"""Data sets from Devore's "Prob and Stat for Eng (7th ed)"

	Data sets and sample analyses from Jay L. Devore (2008),
        "Probability and Statistics for Engineering and the Sciences
        (7th ed)", Thomson.
	"""
	
	cran = "Devore7" 

	version("0.7.6", md5="2e207b4b9ce84b3e172e48930d6ac11e", url="https://cran.r-project.org/src/contrib/Devore7_0.7.6.tar.gz")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
