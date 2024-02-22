# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPixels(RPackage):
	"""Tools for Working with Image Pixels

	Provides tools to show and draw image pixels using 'HTML' widgets 
  and 'Shiny' applications.  It can be used to visualize the 'MNIST' dataset
  for handwritten digit recognition or to create new image recognition datasets.
	"""
	
	homepage = "https://github.com/javierluraschi/pixels"
	cran = "pixels" 

	version("0.1.1", md5="4940a09080aeb57b9051c83de7a78c00")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-miniui", type=("build", "run"))
