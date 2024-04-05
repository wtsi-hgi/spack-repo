# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummer(RPackage):
	"""Small-Area-Estimation Unit/Area Models and Methods for
Estimation in R

	Provides methods for spatial and spatio-temporal smoothing of demographic and health indicators using survey data, with particular focus on estimating and projecting under-five mortality rates, described in Mercer et al. (2015) <doi:10.1214/15-AOAS872>, Li et al. (2019) <doi:10.1371/journal.pone.0210645>, Wu et al. (DHS Spatial Analysis Reports No. 21, 2021), and Li et al. (2023) <arXiv:2007.05117>. 
	"""
	
	homepage = "https://github.com/richardli/SUMMER"
	cran = "SUMMER" 

	version("1.4.0", md5="b115a24f8dffc486ca4c75c1ff49d089")
	version("1.3.0", md5="2eae56d0d46f8b6cde24baf4dff3d8aa")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-shadowtext", type=("build", "run"))
	depends_on("r-ggridges", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-haven", type=("build", "run"))
