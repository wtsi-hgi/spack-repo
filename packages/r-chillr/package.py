# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChillr(RPackage):
	"""Statistical Methods for Phenology Analysis in Temperate Fruit
Trees

	The phenology of plants (i.e. the timing of their annual life
    phases) depends on climatic cues. For temperate trees and many other plants,
    spring phases, such as leaf emergence and flowering, have been found to result
    from the effects of both cool (chilling) conditions and heat. Fruit tree
    scientists (pomologists) have developed some metrics to quantify chilling
    and heat (e.g. see Luedeling (2012) <doi:10.1016/j.scienta.2012.07.011>).
    'chillR' contains functions for processing temperature records into
    chilling (Chilling Hours, Utah Chill Units and Chill Portions) and heat units
    (Growing Degree Hours). Regarding chilling metrics, Chill Portions are often
    considered the most promising, but they are difficult to calculate. This package
    makes it easy. 'chillR' also contains procedures for conducting a PLS analysis
    relating phenological dates (e.g. bloom dates) to either mean temperatures or
    mean chill and heat accumulation rates, based on long-term weather and phenology
    records (Luedeling and Gassner (2012) <doi:10.1016/j.agrformet.2011.10.020>).
    As of version 0.65, it also includes functions for generating weather
    scenarios with a weather generator, for conducting climate change analyses
    for temperature-based climatic metrics and for plotting results from such
    analyses. Since version 0.70, 'chillR' contains a function for interpolating
    hourly temperature records.
	"""
	
	cran = "chillR" 

	version("0.75", md5="f539747202a3241ce0726d551eb37ecf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ecmwfr", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-gensa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-kendall", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rmawgen", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
