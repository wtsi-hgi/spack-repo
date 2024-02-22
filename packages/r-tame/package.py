# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTame(RPackage):
	"""Timing, Anatomical, Therapeutic and Chemical Based Medication
Clustering

	Agglomerative hierarchical clustering with a bespoke distance 
  measure based on medication similarities in the Anatomical Therapeutic 
  Chemical Classification System, medication timing and 
  medication amount or dosage. Tools for summarizing, illustrating and 
  manipulating the cluster objects are also available.
	"""
	
	cran = "tame" 

	version("0.0.1", md5="e156cbdd68e2c964ee9b3e818ae284bd")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fuzzyjoin", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
