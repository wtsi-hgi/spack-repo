# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFruclimadapt(RPackage):
	"""Evaluation Tools for Assessing Climate Adaptation of Fruit Tree
Species

	Climate is a critical component limiting growing range of plant species, which
    also determines cultivar adaptation to a region. The evaluation of climate influence on
    fruit production is critical for decision-making in the design stage of orchards and 
    vineyards and in the evaluation of the potential consequences of future climate. Bio-
    climatic indices and plant phenology are commonly used to describe the suitability of 
    climate for growing quality fruit and to provide temporal and spatial information about 
    regarding ongoing and future changes. 'fruclimadapt' streamlines the assessment of 
    climate adaptation and the identification of potential risks for grapevines and fruit 
    trees. Procedures in the package allow to i) downscale daily meteorological variables
    to hourly values (Forster et al (2016) <doi:10.5194/gmd-9-2315-2016>),
    ii) estimate chilling and forcing heat accumulation (Miranda et al (2019)
    <https://ec.europa.eu/eip/agriculture/sites/default/files/fg30_mp5_phenology_critical_temperatures.pdf>),
    iii) estimate plant phenology (Schwartz (2012) <doi:10.1007/978-94-007-6925-0>), iv) 
    calculate bioclimatic indices to evaluate fruit tree and grapevine adaptation (e.g. Badr 
    et al (2017) <doi:10.3354/cr01532>), v) estimate the incidence of weather-related disorders 
    in fruits (e.g. Snyder and de Melo-Abreu (2005, ISBN:92-5-105328-6) and vi)
    estimate plant water requirements (Allen et al (1998, ISBN:92-5-104219-5)). 
	"""
	
	cran = "fruclimadapt" 

	version("0.4.5", md5="0a171583e716cea708f802d585fe87eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
