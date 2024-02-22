# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeojsonr(RPackage):
	"""A GeoJson Processing Toolkit

	Includes functions for processing GeoJson objects <https://en.wikipedia.org/wiki/GeoJSON> relying on 'RFC 7946' <https://datatracker.ietf.org/doc/pdf/rfc7946.pdf>. The geojson encoding is based on 'json11', a tiny JSON library for 'C++11' <https://github.com/dropbox/json11>. Furthermore, the source code is exported in R through the 'Rcpp' and 'RcppArmadillo' packages.
	"""
	
	homepage = "https://github.com/mlampros/geojsonR"
	cran = "geojsonR" 

	version("1.1.1", md5="1f54f0edcc75e3719b81fe791604760b")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.6:", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
