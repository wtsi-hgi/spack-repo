# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPas(RPackage):
	"""Polygenic Analysis System (PAS)

	An R package for polygenic trait analysis. 
	"""
	
	homepage = "http://statgen.ucr.edu"
	cran = "PAS" 

	version("1.2.5", md5="67f87c816898a678e96980919404972a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
