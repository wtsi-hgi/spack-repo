# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcsscore(RPackage):
	"""GCSscore: an R package for microarray analysis for Affymetrix/Thermo Fisher arrays

	For differential expression analysis of 3'IVT and WT-style microarrays from Affymetrix/Thermo-Fisher.  Based on S-score algorithm originally described by Zhang et al 2002.
	"""
	
	bioc = "GCSscore" 

	version("1.16.0", commit="531fc1b096cbed189a9d5b85c79a2d7b713cc3cc")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-dplr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-affxparser", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
