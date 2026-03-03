# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenofit(RPackage):
	"""Extract Remote Sensing Vegetation Phenology

	
    The merits of 'TIMESAT' and 'phenopix' are adopted. Besides, a simple and 
    growing season dividing method and a practical snow elimination method 
    based on Whittaker were proposed. 7 curve fitting methods and 4 phenology 
    extraction methods were provided. Parameters boundary are considered for 
    every curve fitting methods according to their ecological meaning. 
    And 'optimx' is used to select best optimization method for different 
    curve fitting methods.
    Reference:
    Kong, D., (2020). R package: A state-of-the-art Vegetation Phenology extraction 
    package, phenofit version 0.3.1, <doi:10.5281/zenodo.5150204>;
    Kong, D., Zhang, Y., Wang, D., Chen, J., & Gu, X. (2020). Photoperiod Explains 
    the Asynchronization Between Vegetation Carbon Phenology and Vegetation Greenness 
    Phenology. Journal of Geophysical Research: Biogeosciences, 125(8), e2020JG005636. 
    <doi:10.1029/2020JG005636>;
    Kong, D., Zhang, Y., Gu, X., & Wang, D. (2019). A robust method for reconstructing 
    global MODIS EVI time series on the Google Earth Engine. 
    ISPRS Journal of Photogrammetry and Remote Sensing, 155, 13–24;
    Zhang, Q., Kong, D., Shi, P., Singh, V.P., Sun, P., 2018. Vegetation phenology 
    on the Qinghai-Tibetan Plateau and its response to climate change (1982–2013). 
    Agric. For. Meteorol. 248, 408–417. <doi:10.1016/j.agrformet.2017.10.026>.
	"""
	
	homepage = "https://github.com/eco-hydro/phenofit"
	cran = "phenofit" 

	version("0.3.9", md5="04c848fd41fe9442daeda8814e91e59e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
	depends_on("r-ucminf", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-zeallot", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
