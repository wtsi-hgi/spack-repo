# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighriskzone(RPackage):
	"""Determining and Evaluating High-Risk Zones

	Functions for determining and evaluating high-risk zones and
    simulating and thinning point process data, as described in 'Determining
    high risk zones using point process methodology - Realization by building
    an R package' Seibold (2012) <http://highriskzone.r-forge.r-project.org/Bachelorarbeit.pdf> 
    and 'Determining high-risk zones for unexploded World War II bombs by using point 
    process methodology', Mahling et al. (2013) <doi:10.1111/j.1467-9876.2012.01055.x>.
	"""
	
	cran = "highriskzone" 

	version("1.4.9", md5="150fe0cc7de4543e9d457efd1e497a71")

	depends_on("r-fields", type=("build", "run"))
	depends_on("r-spatstat@1.54.0:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-deldir", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-spatstat-random", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat-explore", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
	depends_on("r-polyclip", type=("build", "run"))
