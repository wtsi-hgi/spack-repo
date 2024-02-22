# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhytoclass(RPackage):
	"""Estimate Chla Biomass of Phytoplankton Groups

	Determine the chlorophyll a (Chl a) biomass of different 
    phytoplankton groups based on their pigment biomarkers. The method uses
    non-negative matrix factorisation and simulated annealing to minimise error
    between the observed and estimated values of pigment concentrations
    (Hayward et al. (2023) <doi:10.1002/lom3.10541>).
    The approach is similar to the widely used 'CHEMTAX' program
    (Mackey et al. 1996) <doi:10.3354/meps144265>, but is more straightforward,
    accurate, and not reliant on initial guesses for the pigment to Chl a
    ratios for each phytoplankton group.
	"""
	
	cran = "phytoclass" 

	version("1.0.0", md5="0465e2390cc898e4b397555da6f83bbe")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bestnormalize", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-metrics", type=("build", "run"))
	depends_on("r-rcppml", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
