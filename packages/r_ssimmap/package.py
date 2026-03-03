# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsimmap(RPackage):
	"""The Structural Similarity Index Measure for Maps

	Extends the classical SSIM method proposed by 'Wang', 'Bovik', 'Sheikh', and 'Simoncelli'(2004) <doi:10.1109/TIP.2003.819861>. 
  for irregular lattice-based maps and raster images.
  The geographical SSIM method incorporates well-developed 'geographically weighted summary statistics'('Brunsdon', 'Fotheringham' and 'Charlton' 2002) <doi:10.1016/S0198-9715(01)00009-6> 
  with an adaptive bandwidth kernel function for irregular lattice-based maps.
	"""
	
	homepage = "https://github.com/Hailyee-Ha/SSIMmap"
	cran = "SSIMmap" 

	version("0.1.1", md5="ff654bfcea1d380a010727024d1512fd")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
