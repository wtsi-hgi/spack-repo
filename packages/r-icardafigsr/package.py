# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcardafigsr(RPackage):
	"""Subsetting using Focused Identification of the Germplasm
Strategy (FIGS)

	Running Focused Identification of the Germplasm Strategy (FIGS) to make best subsets from Genebank Collection.
	"""
	
	cran = "icardaFIGSr" 

	version("1.0.2", md5="1e1ba636b9f6f73d7ae6df03009ce1ec")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plotroc", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
