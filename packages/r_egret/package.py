# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgret(RPackage):
	"""Exploration and Graphics for RivEr Trends

	Statistics and graphics for streamflow history,
    water quality trends, and the statistical modeling algorithm: Weighted
    Regressions on Time, Discharge, and Season (WRTDS). 
	"""
	
	homepage = "https://pubs.usgs.gov/tm/04/a10/"
	cran = "EGRET" 

	version("3.0.9", md5="adaf925274d080282db88f8e5a95c678")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dataretrieval@2.0.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
