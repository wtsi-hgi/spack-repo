# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarpSnowprofilePyface(RPackage):
	"""'python' Modules from Snowpack and Avalanche Research

	
    The development of post-processing functionality for simulated snow profiles 
    by the snow and avalanche community is often done in 'python'. This package
    aims to make these tools accessible to 'R' users. Currently integrated modules 
    contain functions to calculate dry snow layer instabilities in support of
    avalache hazard assessments following the publications of  Richter, Schweizer, 
    Rotach, and Van Herwijnen (2019) <doi:10.5194/tc-13-3353-2019>, and Mayer, 
    Van Herwijnen, Techel, and Schweizer (2022) <doi:10.5194/tc-2022-34>.
	"""
	
	homepage = "http://www.avalancheresearch.ca"
	cran = "sarp.snowprofile.pyface" 

	version("0.1.3", md5="c6b522af861aa93ccb7c69e266e406cd")

	depends_on("r-sarp-snowprofile@1.3:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
