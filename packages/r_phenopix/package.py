# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhenopix(RPackage):
	"""Process Digital Images of a Vegetation Cover

	A collection of functions to process digital images, depict greenness index trajectories and extract relevant phenological stages. 
	"""
	
	cran = "phenopix" 

	version("2.4.4", md5="8b74a5145cfa6cc17918da1435c229ee")

	depends_on("r@2.15.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-stringr@1:", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
