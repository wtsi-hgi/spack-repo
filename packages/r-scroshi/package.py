# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScroshi(RPackage):
	"""Robust Supervised Hierarchical Identification of Single Cells

	Identifying cell types based on expression profiles is a pillar of single cell analysis. 'scROSHI' identifies cell types based on expression profiles of single cell analysis by utilizing previously obtained cell type specific gene sets. It takes into account the hierarchical nature of cell type relationship and does not require training or annotated data. A detailed description of the method can be found at: Prummer, Bertolini, Bosshard, Barkmann, Yates, Boeva, The Tumor Profiler Consortium, Stekhoven, and Singer (2022) <doi:10.1101/2022.04.05.487176>.
	"""
	
	cran = "scROSHI" 

	version("1.0.0.0", md5="98a78cf66484ffaacfc281df168fcfc3")

	depends_on("r@3.60:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-uwot", type=("build", "run"))
