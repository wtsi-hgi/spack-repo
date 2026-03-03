# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiorad(RPackage):
	"""Biological Analysis and Visualization of Weather Radar Data

	Extract, visualize and summarize aerial movements of birds and
    insects from weather radar data. See Dokter, A. M. et al. (2018) 
    "bioRad: biological analysis and visualization of weather radar data" <doi:10.1111/ecog.04028>
    for a software paper describing package and methodologies.
	"""
	
	homepage = "https://github.com/adokter/bioRad/"
	cran = "bioRad" 

	version("0.7.3", md5="091d0b456942cf7bb49dfb41d5f1110e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-frictionless", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lutz", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-suntools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
