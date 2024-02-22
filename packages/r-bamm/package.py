# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamm(RPackage):
	"""Species Distribution Models as a Function of Biotic, Abiotic and
Movement Factors (BAM)

	Species Distribution Modeling (SDM) is a practical methodology 
 that aims to estimate the area of distribution of a species. However, 
 most of the work has focused on estimating static expressions of the 
 correlation between environmental variables. The outputs of
 correlative species distribution models can be interpreted 
 as maps of the suitable environment for a species but not generally as maps
 of its actual distribution. 
 Soberón and Peterson (2005) <doi:10.17161/bi.v2i0.4> presented
 the BAM scheme, a heuristic framework that states that the occupied area of 
 a species occurs on sites that have been accessible through dispersal (M) and 
 have both favorable biotic (B) and abiotic conditions (A). 
 The 'bamm' package implements classes and functions to operate on each element 
 of the BAM and by using a cellular automata model where the occupied area 
 of a species at time t is estimated by the multiplication of three 
 binary matrices: one matrix represents movements (M), another 
 abiotic -niche- tolerances (A), and a third, biotic interactions (B). 
 The theoretical background of the package can be found in 
 Soberón and Osorio-Olvera (2022) <arXiv:2212.06308>.
	"""
	
	homepage = "https://luismurao.github.io/bamm/"
	cran = "bamm" 

	version("0.4.3", md5="203a06237c83062e81f9541f31ae3370")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-raster@3.4.13:", type=("build", "run"))
	depends_on("r-matrix@1.2.14:", type=("build", "run"))
	depends_on("r-rspectra@0.13.1:", type=("build", "run"))
	depends_on("r-magrittr@1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-purrr@0.2:", type=("build", "run"))
	depends_on("r-igraph@1.2:", type=("build", "run"))
	depends_on("r-leaflet@2:", type=("build", "run"))
	depends_on("r-rdpack@0.11:", type=("build", "run"))
	depends_on("r-animation@2.3:", type=("build", "run"))
	depends_on("r-future@1.18:", type=("build", "run"))
	depends_on("r-furrr@0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sp@1.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
