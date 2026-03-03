# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNopp(RPackage):
	"""Nash Optimal Party Positions

	Estimation of party/candidate ideological positions
             that correspond to a Nash equilibrium along a 
             one-dimensional space.
	"""
	
	cran = "nopp" 

	version("1.1.2", md5="691c0762ecc4570e4b53723b0baf0049")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mlogit", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
