# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcluster(RPackage):
	"""Functions for the Detection of Spatial Clusters of Diseases

	A set of functions for the detection of spatial clusters
        of disease using count data. Bootstrap is used to estimate
        sampling distributions of statistics.
	"""
	
	cran = "DCluster" 

	version("0.2-10", md5="48808eda85cf2342e7bd13c8c71ec6a5")

	depends_on("r@1.6.2:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
