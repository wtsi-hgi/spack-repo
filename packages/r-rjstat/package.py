# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjstat(RPackage):
	"""Handle 'JSON-stat' Format in R

	Handle 'JSON-stat' format (<https://json-stat.org>) in R.
    Not all features are supported, especially the extensive metadata
    features of 'JSON-stat'.
	"""
	
	homepage = "https://github.com/ajschumacher/rjstat"
	cran = "rjstat" 

	version("0.4.3", md5="28f9beab194dcca14c82b4cda3a17758")

	depends_on("r-jsonlite@0.9.8:", type=("build", "run"))
	depends_on("r-checkmate@1.7:", type=("build", "run"))
