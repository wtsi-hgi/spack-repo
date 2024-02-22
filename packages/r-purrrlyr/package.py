# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPurrrlyr(RPackage):
	"""Tools at the Intersection of 'purrr' and 'dplyr'

	Some functions at the intersection of 'dplyr' and
    'purrr' that formerly lived in 'purrr'.
	"""
	
	homepage = "https://github.com/hadley/purrrlyr"
	cran = "purrrlyr" 

	version("0.0.8", md5="38a745f7b428808b75529801b5992b65")

	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
