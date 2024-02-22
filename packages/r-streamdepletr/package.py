# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStreamdepletr(RPackage):
	"""Estimate Streamflow Depletion Due to Groundwater Pumping

	Implementation of analytical models for estimating streamflow 
    depletion due to groundwater pumping, and other related tools. Functions
    are broadly split into two groups: (1) analytical streamflow depletion
    models, which estimate streamflow depletion for a single stream reach
    resulting from groundwater pumping; and (2) depletion apportionment 
    equations, which distribute estimated streamflow depletion among multiple
    stream reaches within a stream network. See Zipper et al. (2018) <doi:10.1029/2018WR022707>
    for more information on depletion apportionment equations and Zipper et
    al. (2019) <doi:10.1029/2018WR024403> for more information on analytical
    depletion functions, which combine analytical models and depletion apportionment
    equations.
	"""
	
	homepage = "https://github.com/FoundrySpatial/streamDepletr"
	cran = "streamDepletr" 

	version("0.2.0", md5="710f3b7a6d8f8a272b2c229cff9b99e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmpfr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
