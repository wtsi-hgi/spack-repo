# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAudubon(RPackage):
	"""Japanese Text Processing Tools

	A collection of Japanese text processing tools for filling
    Japanese iteration marks, Japanese character type conversions,
    segmentation by phrase, and text normalization which is based on rules
    for the 'Sudachi' morphological analyzer and the 'NEologd' (Neologism
    dictionary for 'MeCab').  These features are specific to Japanese and
    are not implemented in 'ICU' (International Components for Unicode).
	"""
	
	homepage = "https://github.com/paithiov909/audubon"
	cran = "audubon" 

	version("0.5.1", md5="0f9358256232f51c31d1a49c445ab307")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
