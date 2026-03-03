# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwfscmisc(RPackage):
	"""Miscellaneous Functions for Southwest Fisheries Science Center

	Collection of conversion, analytical, geodesic, mapping, and
    plotting functions. Used to support packages and code written by
    researchers at the Southwest Fisheries Science Center of the National
    Oceanic and Atmospheric Administration.
	"""
	
	homepage = "https://github.com/EricArcher/swfscMisc"
	cran = "swfscMisc" 

	version("1.6.5", md5="1a9b59d9348a58be45b5b24fdfd32c5e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-modeest", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-runjags", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
