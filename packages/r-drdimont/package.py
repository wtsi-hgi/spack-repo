# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrdimont(RPackage):
	"""Drug Response Prediction from Differential Multi-Omics Networks

	While it has been well established that drugs affect and help
  patients differently, personalized drug response predictions remain 
  challenging. Solutions based on single omics measurements have been proposed, 
  and networks provide means to incorporate molecular interactions into reasoning. 
  However, how to integrate the wealth of information contained in multiple omics 
  layers still poses a complex problem. 
  We present a novel network analysis pipeline, DrDimont, Drug response prediction 
  from Differential analysis of multi-omics networks. It allows for comparative 
  conclusions between two conditions and translates them into differential drug 
  response predictions. DrDimont focuses on molecular interactions. It establishes 
  condition-specific networks from correlation within an omics layer that are 
  then reduced and combined into heterogeneous, multi-omics molecular networks. 
  A novel semi-local, path-based integration step ensures integrative conclusions. 
  Differential predictions are derived from comparing the condition-specific 
  integrated networks. DrDimont's predictions are explainable, i.e., molecular 
  differences that are the source of high differential drug scores can be retrieved.
  Our proposed pipeline leverages multi-omics data for differential predictions,
  e.g. on drug response, and includes prior information on interactions.
  The case study presented in the vignette uses data published by
  Krug (2020) <doi:10.1016/j.cell.2020.10.036>. The package license applies only
  to the software and explicitly not to the included data.
	"""
	
	cran = "DrDimont" 

	version("0.1.4", md5="e6c8cc1e5b2c0d96aae62c56efb49cf0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-wgcna", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
