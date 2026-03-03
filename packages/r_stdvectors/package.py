# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStdvectors(RPackage):
	"""C++ Standard Library Vectors in R

	Allows the creation and manipulation of C++ std::vector's in R.
	"""
	
	homepage = "https://github.com/digEmAll/stdvectors"
	cran = "stdvectors" 

	version("0.0.5", md5="a4b4bde02d3086f3392537c1b99b667e")

	depends_on("r-rcpp", type=("build", "run"))
