# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRneighborgwas(RPackage):
	"""Testing Neighbor Effects in Marker-Based Regressions

	To incorporate neighbor genotypic identity into genome-wide association studies, the package provides a set of functions for variation partitioning and association mapping. The theoretical background of the method is described in Sato et al. (2021) <doi:10.1038/s41437-020-00401-w>.
	"""
	
	cran = "rNeighborGWAS" 

	version("1.2.4", md5="585e2245d7ed223310b3cd3c4511bfcf")

	depends_on("r-gaston", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
