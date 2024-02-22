# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlexpolyline(RPackage):
	"""Flexible Polyline Encoding

	Binding to the C++ implementation of the flexible polyline
    encoding by HERE <https://github.com/heremaps/flexible-polyline>. The
    flexible polyline encoding is a lossy compressed representation of a list of
    coordinate pairs or coordinate triples. The encoding is achieved by:
    (1) Reducing the decimal digits of each value;
    (2) encoding only the offset from the previous point;
    (3) using variable length for each coordinate delta; and
    (4) using 64 URL-safe characters to display the result.
	"""
	
	homepage = "https://munterfi.github.io/flexpolyline/"
	cran = "flexpolyline" 

	version("0.3.0", md5="e9ea0c52854955fe9d062e0f742f8f63")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf@0.9.3:", type=("build", "run"))
