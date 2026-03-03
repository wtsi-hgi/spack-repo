# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecklestar(RPackage):
	"""Reduction of Speckle Data from BTA 6-m Telescope

	A set of functions for obtaining positional parameters and magnitude difference between components of binary and multiple stellar systems from series of speckle images.
	"""
	
	homepage = "https://drastega.github.io/docs/specklestar_vignette.html"
	cran = "specklestar" 

	version("0.0.1.7", md5="1587cbeb28ecb7da0952a23be8e5fc21")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("fftw@3.1.2:", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
