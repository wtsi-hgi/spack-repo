# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCare4cmodel(RPackage):
	"""Carbon-Related Assessment of Silvicultural Concepts

	A simulation model and accompanying functions that support 
    assessing silvicultural concepts on the forest estate level with a focus on 
    the CO2 uptake by wood growth and CO2 emissions by forest operations. For 
    achieving this, a virtual forest estate area is split into the areas covered
    by typical phases of the silvicultural concept of interest. Given initial 
    area shares of these phases, the dynamics of these areas is simulated. The 
    typical carbon stocks and flows which are known for all phases are 
    attributed post-hoc to the areas and upscaled to the estate level. CO2 
    emissions by forest operations are estimated based on the amounts and 
    dimensions of the harvested timber. Probabilities of damage events are taken
    into account.
	"""
	
	cran = "care4cmodel" 

	version("1.0.1", md5="ac1dc553d2c84da16005ae680ee2c003")
	version("1.0.0", md5="a925f7b29d473b0660786274aa66eb7d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
