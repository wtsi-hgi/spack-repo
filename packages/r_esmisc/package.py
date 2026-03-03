# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsmisc(RPackage):
	"""Misc Functions of Eduard Szöcs

	Misc functions programmed by Eduard Szöcs. 
    Provides read_regnie() to read gridded precipitation data from German Weather 
    Service  (DWD, see <http://www.dwd.de/> for more information).
	"""
	
	homepage = "https://github.com/EDiLD/esmisc"
	cran = "esmisc" 

	version("0.0.3", md5="33fb83a6552714df2760c7984f79d2b1")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
