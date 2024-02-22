# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsims(RPackage):
	"""Distance Sampling Simulations

	Performs distance sampling simulations. 'dsims' repeatedly generates
    instances of a user defined population within a given survey region. It then 
    generates realisations of a survey design and simulates the detection process. 
    The data are then analysed so that the results can be compared for accuracy 
    and precision across all replications. This process allows users to optimise 
    survey designs for their specific set of survey conditions. The effects of 
    uncertainty in population distribution or parameters can be investigated
    under a number of simulations so that users can be confident that they have
    achieved a robust survey design before deploying vessels into the field. The
    distance sampling designs used in this package from 'dssd' are detailed in
    Chapter 7 of Advanced Distance Sampling, Buckland et. al. (2008, ISBN-13: 
    978-0199225873). General distance sampling methods are detailed in Introduction 
    to Distance Sampling: Estimating Abundance of Biological Populations, Buckland 
    et. al. (2004, ISBN-13: 978-0198509271). Find out more about estimating 
    animal/plant abundance with distance sampling at <http://distancesampling.org/>.
	"""
	
	homepage = "https://github.com/DistanceDevelopment/dsims"
	cran = "dsims" 

	version("1.0.4", md5="cdf8ed60da1f43e5f6b525e397352791")

	depends_on("r-dssd@0.2.2:", type=("build", "run"))
	depends_on("r-mrds", type=("build", "run"))
	depends_on("r-distance", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rstudioapi", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
