# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLifemapr(RPackage):
	"""Data Visualisation on 'Lifemap' Tree

	Allow to visualise data on the NCBI phylogenetic tree as presented in Lifemap '<http://lifemap.univ-lyon1.fr/>'. It takes as input a dataframe with at least a "taxid" column containing NCBI format TaxIds and allows to draw multiple layers with different visualisation tools.
	"""
	
	cran = "LifemapR" 

	version("1.0.4", md5="076a4c65761b2ef38e51141a366a2441")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-leaflet-minicharts", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
