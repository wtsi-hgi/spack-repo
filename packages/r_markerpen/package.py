# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarkerpen(RPackage):
	"""Marker Gene Detection via Penalized Principal Component Analysis

	Implementation of the 'MarkerPen' algorithm, short for marker gene detection
    via penalized principal component analysis, described in the paper by Qiu, Wang, Lei,
    and Roeder (2020, <doi:10.1101/2020.11.07.373043>). 'MarkerPen' is a semi-supervised
    algorithm for detecting marker genes by combining prior marker information with bulk
    transcriptome data.
	"""
	
	cran = "markerpen" 

	version("0.1.1", md5="7c03f059cfd3f18e46241176fe11e931")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
