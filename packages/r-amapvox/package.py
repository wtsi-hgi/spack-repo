# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmapvox(RPackage):
	"""LiDAR Data Voxelisation

	Read, manipulate and write voxel spaces. Voxel spaces are
    read from text-based output files of the 'AMAPVox' software. 'AMAPVox'
    is a LiDAR point cloud voxelisation software that aims at estimating
    leaf area through several theoretical/numerical approaches. See more
    in the article Vincent et al. (2017) <doi:10.23708/1AJNMP> and the
    technical note Vincent et al. (2021) <doi:10.23708/1AJNMP>.
	"""
	
	homepage = "https://amapvox.org"
	cran = "AMAPVox" 

	version("1.0.1", md5="af63a54b02ce3e86cdd1aceaec4a510d")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
