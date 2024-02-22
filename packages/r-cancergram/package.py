# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCancergram(RPackage):
	"""Prediction of Anticancer Peptides

	Predicts anticancer peptides using random forests trained on the
    n-gram encoded peptides. The implemented algorithm can be accessed from
    both the command line and shiny-based GUI. The CancerGram model is too large 
    for CRAN and it has to be downloaded separately from the repository:
    <https://github.com/BioGenies/CancerGramModel>. For more information see: 
    Burdukiewicz et al. (2020) <doi:10.3390/pharmaceutics12111045>. 
	"""
	
	homepage = "https://github.com/BioGenies/CancerGram"
	cran = "CancerGram" 

	version("1.0.0", md5="4e9a9785af2a08d859bbfdce507551a3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biogram", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
