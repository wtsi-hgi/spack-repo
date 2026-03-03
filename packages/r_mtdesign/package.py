# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtdesign(RPackage):
	"""Mander and Thompson Designs

	Implements Mander & Thompson's (2010) 
    <doi:10.1016/j.cct.2010.07.008> methods for two-stage designs
    optimal under the alternative hypothesis for phase II [cancer] trials.  Also
    provides an implementation of Simon's (1989) 
    <doi:10.1016/0197-2456(89)90015-9> original methodology and 
    allows exploration of the operating characteristics of sub-optimal designs.
	"""
	
	homepage = "https://github.com/openpharma/mtdesign"
	cran = "mtdesign" 

	version("0.1.0", md5="58ea9c73dd68dd45b323cc0b39c13e62")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
