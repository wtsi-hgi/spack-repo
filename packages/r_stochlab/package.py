# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStochlab(RPackage):
	"""Stochastic Collision Risk Model

	Collision Risk Models for avian fauna (seabird and migratory birds) at
    offshore wind farms. The base deterministic model is derived from 
    Band (2012) <https://tethys.pnnl.gov/publications/using-collision-risk-model-assess-bird-collision-risks-offshore-wind-farms>. 
    This was further expanded on by Masden (2015) <doi:10.7489/1659-1> and code 
    used here is heavily derived from this work with input from Dr A. Cook at the 
    British Trust for Ornithology. These collision risk models are useful for 
    marine ornithologists who are working in the offshore wind industry, particularly 
    in UK waters. However, many of the species included in the stochastic collision 
    risk models can also be found in the North Atlantic in the 
    United States and Canada, and could be applied there. 
	"""
	
	homepage = "https://github.com/HiDef-Aerial-Surveying/stochLAB"
	cran = "stochLAB" 

	version("1.1.2", md5="f74e022be0f086e7cf99111944595c0d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-logr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
