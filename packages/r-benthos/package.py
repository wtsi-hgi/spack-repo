# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBenthos(RPackage):
	"""Marine Benthic Ecosystem Analysis

	Preprocessing tools and biodiversity measures 
    (species abundance, species richness, population heterogeneity and 
    sensitivity) for analysing marine benthic data. See Van Loon et al.
    (2015) <doi:10.1016/j.seares.2015.05.002> for an application of 
    these tools.
	"""
	
	cran = "benthos" 

	version("1.3-8", md5="d65fa0a0c749d020811dc5eb06bbdc73")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
