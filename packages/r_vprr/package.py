# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVprr(RPackage):
	"""Processing and Visualization of Video Plankton Recorder Data

	An oceanographic data processing package for analyzing and visualizing Video 
    Plankton Recorder data.  This package was developed at 'Bedford Institute of Oceanography'.
    Functions are designed to process automated image classification output and create organized and 
    easily portable data products.
	"""
	
	homepage = "https://eogrady21.github.io/vprr/"
	cran = "vprr" 

	version("0.2.3", md5="0c4ec8d66f96d3634d384dc25b222449")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-oce", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-gsw", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-cmocean", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-usethis", type=("build", "run"))
