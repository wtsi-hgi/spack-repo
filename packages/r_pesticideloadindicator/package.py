# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPesticideloadindicator(RPackage):
	"""Computes Danish Pesticide Load Indicator

	Computes the Danish Pesticide Load Indicator as described in Kudsk et al. (2018) <doi:10.1016/j.landusepol.2017.11.010> and Moehring et al. (2019) <doi:10.1016/j.scitotenv.2018.07.287> for pesticide use data. Additionally offers the possibility to directly link pesticide use data to pesticide properties given access to the Pesticide properties database (Lewis et al., 2016) <doi:10.1080/10807039.2015.1133242>. 
	"""
	
	cran = "PesticideLoadIndicator" 

	version("1.3.1", md5="2759943425105ead1885b07f7aee4a8a")

	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
