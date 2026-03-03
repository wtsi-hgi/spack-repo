# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilink(RPackage):
	"""Multifile Record Linkage and Duplicate Detection

	Implementation of the methodology of Aleshin-Guendel & Sadinle (2022) <doi:10.1080/01621459.2021.2013242>. It handles the general problem of multifile record linkage and duplicate detection, where any number of files are to be linked, and any of the files may have duplicates.
	"""
	
	homepage = "https://github.com/aleshing/multilink"
	cran = "multilink" 

	version("0.1.1", md5="f7eb90c87e52719050c8b7842a227162")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-recordlinkage", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-mcclust", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
