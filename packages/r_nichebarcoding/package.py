# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNichebarcoding(RPackage):
	"""Niche-model-Based Species Identification

	Species Identification using DNA Barcodes Integrated with 
             Environmental Niche Models.
	"""
	
	homepage = "https://github.com/Yangcq-Ivy/NicheBarcoding"
	cran = "NicheBarcoding" 

	version("1.0", md5="c66675b25e07fecf731458f5534a2fd5")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-dismo", type=("build", "run"))
	depends_on("r-e1071@1.7.7:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-spider", type=("build", "run"))
	depends_on("r-vegan", type=("build", "run"))
