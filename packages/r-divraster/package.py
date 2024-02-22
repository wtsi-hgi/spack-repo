# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDivraster(RPackage):
	"""Diversity Metrics Calculations for Rasterized Data

	Alpha and beta diversity for taxonomic (TD), functional (FD), and phylogenetic (PD) dimensions based on rasters. Spatial and temporal beta diversity can be partitioned into replacement and richness difference components. It also calculates standardized effect size for FD and PD alpha diversity and the average individual traits across multilayer rasters. The layers of the raster represent species, while the cells represent communities. Methods details can be found at Cardoso et al. 2022 <https://CRAN.R-project.org/package=BAT> and Heming et al. 2023 <https://CRAN.R-project.org/package=SESraster>.
	"""
	
	homepage = "https://github.com/flaviomoc/divraster"
	cran = "divraster" 

	version("1.0.4", md5="d1fedc37574d14b4503daad4e685880b")

	depends_on("r-bat", type=("build", "run"))
	depends_on("r-sesraster", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
