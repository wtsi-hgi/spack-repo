# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptimosPrime(RPackage):
	"""Optimos Prime Helps Calculate Autoecological Data for Biological
Species

	Calculates autoecological data (optima and tolerance ranges) of a biological species
    given an environmental matrix. The package calculates by weighted averaging, using the number of occurrences to adjust the 
    tolerance assigned to each taxon to estimate optima and tolerance range in cases where taxa 
    have unequal occurrences. See the detailed methodology by Birks et al. (1990) <doi:10.1098/rstb.1990.0062>, and a 
    case example by Potapova and Charles (2003) <doi:10.1046/j.1365-2427.2003.01080.x>.
	"""
	
	cran = "optimos.prime" 

	version("0.1.2", md5="14f27aeead95ce658a11eb2350bc3e15")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
