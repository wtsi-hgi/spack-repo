# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRapsimng(RPackage):
	"""APSIM Next Generation

	The Agricultural Production Systems sIMulator ('APSIM') is a widely
    used to simulate the agricultural systems for multiple crops. This package 
    is designed to create, modify and run 'apsimx' files in the 'APSIM' Next 
    Generation <https://www.apsim.info/>.
	"""
	
	homepage = "https://rapsimng.bangyou.me/"
	cran = "rapsimng" 

	version("0.4.4", md5="1968ee3c40d29a979133e20ac7cb978e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
