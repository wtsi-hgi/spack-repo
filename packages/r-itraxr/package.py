# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RItraxr(RPackage):
	"""Itrax Data Analysis Tools

	Parse, trim, join, visualise and analyse data from Itrax sediment core multi-parameter 
    scanners manufactured by Cox Analytical Systems, Sweden. Functions are provided for parsing 
    XRF-peak area files, line-scan optical images, and radiographic images, alongside accompanying metadata. 
    A variety of data wrangling tasks like trimming, joining and reducing XRF-peak area data are simplified. 
    Multivariate methods are implemented with appropriate data transformation. 
	"""
	
	homepage = "https://github.com/tombishop1/itraxR/"
	cran = "itraxR" 

	version("1.12.1", md5="52fa9bc3fa8db3b9d2ee35cd4d032dae")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-ggcorrplot", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-munsellinterpol", type=("build", "run"))
