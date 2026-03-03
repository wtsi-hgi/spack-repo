# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtdemo(RPackage):
	"""Item Response Theory Demo Collection

	
  Includes a collection of shiny applications to demonstrate
  or to explore fundamental item response theory (IRT) concepts
  such as estimation, scoring, and multidimensional IRT models.
	"""
	
	cran = "irtDemo" 

	version("0.1.4", md5="bbedb8c79929c13398416a16a63499eb")

	depends_on("r@3.2.4:", type=("build", "run"))
	depends_on("r-shiny@0.13.2:", type=("build", "run"))
	depends_on("r-fgarch@3010.82:", type=("build", "run"))
