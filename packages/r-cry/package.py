# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCry(RPackage):
	"""Statistics for Structural Crystallography

	Reading and writing of files in the most commonly used formats of
  structural crystallography. It includes functions to work with a variety
  of statistics used in this field and functions to perform basic
  crystallographic computing. References: D. G. Waterman, J. Foadi, G. Evans 
  (2011) <doi:10.1107/S0108767311084303>.
	"""
	
	homepage = "https://jfoadi.github.io/cry/"
	cran = "cry" 

	version("0.5.1", md5="0e0a33f350242bbd79592dd481da4dff")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
