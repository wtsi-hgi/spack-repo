# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrcme(RPackage):
	"""Order Restricted Clustering for Microarray Experiments

	Provides clustering of genes with similar 
  dose response (or time course) profiles. It implements the method 
  described by Lin et al. (2012).
	"""
	
	cran = "ORCME" 

	version("2.0.2", md5="735283f8bee62bf430180975b1a7616f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
