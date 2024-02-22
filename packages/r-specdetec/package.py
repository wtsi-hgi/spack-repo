# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpecdetec(RPackage):
	"""Change Points Detection with Spectral Clustering

	Calculate change point based on spectral clustering with the option to automatically calculate the number of clusters if this information is not available.
	"""
	
	cran = "SpecDetec" 

	version("1.0.0", md5="af76c21123564f1843a02bf4e1105e38")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
