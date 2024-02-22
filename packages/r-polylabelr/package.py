# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolylabelr(RPackage):
	"""Find the Pole of Inaccessibility (Visual Center) of a Polygon

	A wrapper around the C++ library 'polylabel' from 'Mapbox', 
    providing an efficient routine for finding the approximate pole of 
    inaccessibility of a polygon, which usually serves as an excellent candidate
    for labeling of a polygon.
	"""
	
	homepage = "https://github.com/jolars/polylabelr"
	cran = "polylabelr" 

	version("0.2.0", md5="f6f728305406ad9180b18c8c66c5846b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
