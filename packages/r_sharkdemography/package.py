# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSharkdemography(RPackage):
	"""Shark Demographic Analyses Using Leslie Matrix Models

	Run Leslie Matrix models using Monte Carlo simulations for any specified shark species. 
    This package was developed during the publication of Smart, JJ, White, WT, Baje, L, et al. (2020)
    "Can multi-species shark longline fisheries be managed sustainably using size limits? 
    Theoretically, yes. Realistically, no".J Appl Ecol. 2020; 57; 1847–1860. 
    <doi:10.1111/1365-2664.13659>.
	"""
	
	homepage = "https://github.com/jonathansmart/SharkDemography"
	cran = "SharkDemography" 

	version("1.1.0", md5="d1818fb021cb937c313d0d3631265c85")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-popbio", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
