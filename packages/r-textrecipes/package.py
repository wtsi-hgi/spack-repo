# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextrecipes(RPackage):
	"""Extra 'Recipes' for Text Processing

	Converting text to numerical features requires specifically
    created procedures, which are implemented as steps according to the
    'recipes' package. These steps allows for tokenization, filtering,
    counting (tf and tfidf) and feature hashing.
	"""
	
	homepage = "https://github.com/tidymodels/textrecipes"
	cran = "textrecipes" 

	version("1.0.6", md5="45fd8ccfc9310940aa08132ae456ee22")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-recipes@1.0.7:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-generics@0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tokenizers", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
