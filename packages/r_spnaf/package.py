# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpnaf(RPackage):
	"""Spatial Network Autocorrelation for Flow Data

	Identify statistically significant flow clusters using the local spatial network autocorrelation statistic G_ij* 
    proposed by 'Berglund' and 'Karlström' (1999) <doi:10.1007/s101090050013>. 
    The metric, an extended statistic of 'Getis/Ord' G ('Getis' and 'Ord' 1992) <doi:10.1111/j.1538-4632.1992.tb00261.x>, 
    detects a group of flows having similar traits in terms of directionality. 
    You provide OD data and the associated polygon to get results 
    with several parameters, some of which are defined by spdep package.
	"""
	
	cran = "spnaf" 

	version("0.3.1", md5="2b374c13e4c4de8866f9f5b025d4a75d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
