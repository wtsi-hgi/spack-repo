# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReddyproc(RPackage):
	"""Post Processing of (Half-)Hourly Eddy-Covariance Measurements

	Standard and extensible Eddy-Covariance data post-processing 
  (Wutzler et al. (2018) <doi:10.5194/bg-15-5015-2018>)
  includes  
  uStar-filtering, gap-filling, and flux-partitioning.
  The Eddy-Covariance (EC)  micrometeorological technique quantifies continuous 
  exchange fluxes of gases, energy, and momentum between an ecosystem and the atmosphere.
  It is important for understanding ecosystem dynamics and upscaling exchange fluxes.
  (Aubinet et al. (2012) <doi:10.1007/978-94-007-2351-1>).
  This package inputs pre-processed (half-)hourly data and supports further processing. 
  First, a quality-check and filtering is performed based on the relationship between 
  measured flux and friction
  velocity (uStar) to discard biased data 
  (Papale et al. (2006) <doi:10.5194/bg-3-571-2006>).
  Second, gaps in the data are filled based on information from environmental conditions
  (Reichstein et al. (2005) <doi:10.1111/j.1365-2486.2005.001002.x>).
  Third, the net flux of carbon dioxide is partitioned
  into its gross fluxes in and out of the ecosystem by night-time 
  based and day-time based approaches
  (Lasslop et al. (2010) <doi:10.1111/j.1365-2486.2009.02041.x>).
	"""
	
	homepage = "https://www.bgc-jena.mpg.de/bgi/index.php/Services/REddyProcWeb"
	cran = "REddyProc" 

	version("1.3.3", md5="a79d9f7fc86ec1f683ce00e87e011461")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-solartime", type=("build", "run"))
	depends_on("r-bigleaf@0.7:", type=("build", "run"))
	depends_on("r-mlegp", type=("build", "run"))
