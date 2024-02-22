# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfhotspot(RPackage):
	"""Hot-Spot Analysis with Simple Features

	Identify and understand clusters of points (typically representing 
    the locations of places or events) stored in simple-features (SF) objects.
    This is useful for analysing, for example, hot-spots of crime events. The 
    package emphasises producing results from point SF data in a single step 
    using reasonable default values for all other arguments, to aid rapid data 
    analysis by users who are starting out. Functions available include kernel
    density estimation (for details, see Yip (2020) 
    <doi:10.22224/gistbok/2020.1.12>), analysis of spatial association (Getis
    and Ord (1992) <doi:10.1111/j.1538-4632.1992.tb00261.x>) and hot-spot
    classification (Chainey (2020) ISBN:158948584X).
	"""
	
	homepage = "http://pkgs.lesscrime.info/sfhotspot/"
	cran = "sfhotspot" 

	version("0.8.0", md5="9ee3671fd25b52ce2e9a2ee9f0870306")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spatialkde", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
