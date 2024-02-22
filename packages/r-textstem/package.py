# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextstem(RPackage):
	"""Tools for Stemming and Lemmatizing Text

	Tools that stem and lemmatize text.  Stemming is a process that removes
         endings such as affixes.  Lemmatization is the process of grouping inflected
         forms together as a single base form.
	"""
	
	homepage = "http://github.com/trinker/textstem"
	cran = "textstem" 

	version("0.1.4", md5="73bc1704ef5d7ae2fd32aba3062aae4c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-korpus-lang-en", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-hunspell", type=("build", "run"))
	depends_on("r-korpus", type=("build", "run"))
	depends_on("r-lexicon@0.4.1:", type=("build", "run"))
	depends_on("r-quanteda@0.99.12:", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-textclean", type=("build", "run"))
	depends_on("r-textshape", type=("build", "run"))
