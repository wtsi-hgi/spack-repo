# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpaimer(RPackage):
	"""Assess the Diagnostic Power of Genomic Marker Combinations

	Population genetics package for designing diagnostic panels. 
    Candidate markers, marker combinations, and different panel sizes are 
    assessed for how well they can predict the source population of known 
    samples. Requires a genotype file of candidate markers in STRUCTURE format. 
    Methods for population cross-validation are described in Jombart (2008) 
    <doi:10.1093/bioinformatics/btn129>.
	"""
	
	homepage = "https://github.com/OksanaVe/snpAIMeR"
	cran = "snpAIMeR" 

	version("2.1.1", md5="f54e848a982937a2b4c6c95d5356a615")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
