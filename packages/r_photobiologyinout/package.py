# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhotobiologyinout(RPackage):
	"""Read Spectral and Logged Data from Foreign Files

	Functions for reading, and in some cases writing, foreign files 
    containing spectral data from spectrometers and their associated software, 
    output from daylight simulation models in common use, and some spectral 
    data repositories. As well as functions for exchange of spectral data with 
    other R packages. Part of the 'r4photobiology' suite, 
    Aphalo P. J. (2015) <doi:10.19232/uv4pb.2015.1.14>.
	"""
	
	homepage = "https://docs.r4photobiology.info/photobiologyInOut/"
	cran = "photobiologyInOut" 

	version("0.4.27", md5="23a07474dd0e6b234faef7eb0748e448")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-photobiology@0.10.15:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
	depends_on("r-lubridate@1.9.2:", type=("build", "run"))
	depends_on("r-anytime@0.3.9:", type=("build", "run"))
	depends_on("r-tibble@3.2.1:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-readr@2.1.4:", type=("build", "run"))
	depends_on("r-readxl@1.4.3:", type=("build", "run"))
	depends_on("r-colorspec@1.4.0:", type=("build", "run"))
