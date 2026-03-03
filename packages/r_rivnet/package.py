# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRivnet(RPackage):
	"""Extract and Analyze Rivers from Elevation Data

	Seamless extraction of river networks from digital 
    elevation models data. The package allows analysis of digital 
	elevation models that can be either externally provided or
	downloaded from open source repositories (thus interfacing
	with the 'elevatr' package). Extraction is performed via the 
	'D8' flow direction algorithm of TauDEM (Terrain Analysis Using 
	Digital Elevation Models), thus interfacing with the 'traudem' 
	package. Resulting river networks are compatible with functions 
	from the 'OCNet' package. See Carraro (2023) 
	<doi:10.5194/hess-27-3733-2023> for a presentation of the package.
	"""
	
	homepage = "https://lucarraro.github.io/rivnet/"
	cran = "rivnet" 

	version("0.4.0", md5="3e5500c7ca7ed9d3193b5a5516f2b36a")

	depends_on("r-spam", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-traudem", type=("build", "run"))
	depends_on("r-elevatr", type=("build", "run"))
	depends_on("r-ocnet@1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
