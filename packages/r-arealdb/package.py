# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArealdb(RPackage):
	"""Harmonise and Integrate Heterogeneous Areal Data

	Many relevant applications in the environmental and socioeconomic 
    sciences use areal data, such as biodiversity checklists, agricultural statistics, 
    or socioeconomic surveys. For applications that surpass the spatial, temporal or 
    thematic scope of any single data source, data must be integrated from several 
    heterogeneous sources. Inconsistent concepts, definitions, or messy data tables 
    make this a tedious and error-prone process. 'arealDB' tackles those problems and 
    helps the user to integrate a harmonised databases of areal data. Read the paper
    at Ehrmann, Seppelt & Meyer (2020) <doi:10.1016/j.envsoft.2020.104799>.
	"""
	
	homepage = "https://github.com/luckinet/arealDB"
	cran = "arealDB" 

	version("0.6.3", md5="f57f9411e596384411e97c1d2bdd7bf8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tabshiftr", type=("build", "run"))
	depends_on("r-ontologics", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rmapshaper", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
