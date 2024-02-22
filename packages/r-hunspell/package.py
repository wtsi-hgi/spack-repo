# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHunspell(RPackage):
	"""High-Performance Stemmer, Tokenizer, and Spell Checker

	Low level spell checker and morphological analyzer based on the 
    famous 'hunspell' library <https://hunspell.github.io>. The package can analyze
    or check individual words as well as parse text, latex, html or xml documents.
    For a more user-friendly interface use the 'spelling' package which builds on
    this package to automate checking of files, documentation and vignettes in all
    common formats.
	"""
	
	homepage = "https://docs.ropensci.org/hunspell/"
	cran = "hunspell" 

	version("3.0.3", md5="8bd560b5bc128d9307a3d0e344a6a9b4")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.12:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
