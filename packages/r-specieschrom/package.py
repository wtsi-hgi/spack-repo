# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecieschrom(RPackage):
	"""The Species Chromatogram

	A simple method to display and characterise the multidimensional ecological niche of a species. The method also estimates the optimums and amplitudes along each niche dimension. Give also an estimation of the degree of niche overlapping between species. See Kleparski and Beaugrand (2022) <doi:10.1002/ece3.8830> for further details. 
	"""
	
	homepage = "https://github.com/loick-klpr/specieschrom"
	cran = "specieschrom" 

	version("1.0.0", md5="3920e8a9a55f5c04a316779e60892d6d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-colorramps", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
