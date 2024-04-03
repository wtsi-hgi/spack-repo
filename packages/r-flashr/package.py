# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlashr(RPackage):
	"""Create Flashcards of Terms and Definitions

	Provides functions for creating flashcard decks of terms and 
    definitions. This package creates HTML slides using 'revealjs' that can be 
    viewed in the 'RStudio' viewer or a web browser.  Users can create 
    flashcards from either existing built-in decks or create their own from CSV
    files or vectors of function names.
	"""
	
	homepage = "https://github.com/JeffreyRStevens/flashr"
	cran = "flashr" 

	version("0.1.1", md5="dfb746e94ada9a3f9aa306c595f4d05f")
	version("0.1.2", md5="8d17d95a33c2203d06e3f4d48b2045b6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-gh", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-revealjs", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
