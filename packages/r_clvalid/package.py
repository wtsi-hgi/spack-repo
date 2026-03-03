# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClvalid(RPackage):
	"""Validation of Clustering Results

	Statistical and biological validation of clustering results. This package implements Dunn Index, Silhouette, Connectivity, Stability, BHI and BSI. Further information can be found in Brock, G et al. (2008) <doi: 10.18637/jss.v025.i04>.
	"""
	
	cran = "clValid" 

	version("0.7", md5="9e7b76ee97d9027dbcaeb5931d583bc9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
