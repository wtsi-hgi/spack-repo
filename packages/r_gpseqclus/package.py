# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpseqclus(RPackage):
	"""Sequential Clustering Algorithm for Location Data

	Applies sequential clustering algorithm to animal location data 
    based on user-defined parameters. Plots interactive cluster maps and 
    provides a summary dataframe with attributes for each cluster commonly
    used as covariates in subsequent modeling efforts. Additional functions
    provide individual keyhole markup language plots for quick assessment,
    and export of global positioning system exchange format files for
    navigation purposes. 
    Methods can be found at <doi:10.1111/2041-210X.13572>.
	"""
	
	cran = "GPSeqClus" 

	version("1.4.0", md5="4cb22be55380f9e25a461d031c18a1ba")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-leaflet-extras", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
