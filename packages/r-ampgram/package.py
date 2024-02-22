# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmpgram(RPackage):
	"""Prediction of Antimicrobial Peptides

	Predicts antimicrobial peptides using random forests trained on the
    n-gram encoded peptides. The implemented algorithm can be accessed from
    both the command line and shiny-based GUI. The AmpGram model is too large 
    for CRAN and it has to be downloaded separately from the repository:
    <https://github.com/michbur/AmpGramModel>.
	"""
	
	homepage = "https://github.com/michbur/AmpGram"
	cran = "AmpGram" 

	version("1.0", md5="cc95d9fd9313564719480ca65b75478d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biogram", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
