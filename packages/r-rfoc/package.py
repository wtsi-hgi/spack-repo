# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfoc(RPackage):
	"""Graphics for Spherical Distributions and Earthquake Focal
Mechanisms

	Graphics for statistics on a sphere, as applied to geological fault data, crystallography, earthquake focal mechanisms, radiation patterns, ternary plots and geographical/geological maps.  Non-double couple plotting of focal spheres and source type maps are included for statistical analysis of moment tensors.
	"""
	
	cran = "RFOC" 

	version("3.4-10", md5="a5fd3395823ad444dbe523b2fa750840")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
	depends_on("r-geomap", type=("build", "run"))
	depends_on("r-rseis", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
