# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpbbm(RPackage):
	"""Dirichlet Process Beta-Binomial Mixture

	Beta-binomial Mixture Model is used to infer the pattern from count data.
		It can be used for clustering of RNA methylation sequencing data. 
	"""
	
	cran = "DPBBM" 

	version("0.2.5", md5="0e65caa1a342e7d50c9e4cc7707344be")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-tmvtnorm", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ceoptim", type=("build", "run"))
