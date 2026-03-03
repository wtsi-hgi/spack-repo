# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPpsfs(RPackage):
	"""Partial Profile Score Feature Selection in High-Dimensional
Generalized Linear Interaction Models

	
    This is an implementation of the partial profile score feature 
    selection (PPSFS) approach to generalized linear (interaction) models. 
    The PPSFS is highly scalable even for ultra-high-dimensional feature space. 
    See the paper by Xu, Luo and Chen (2021, <doi:10.4310/21-SII706>).
	"""
	
	homepage = "https://github.com/paradoxical-rhapsody/PPSFS"
	cran = "PPSFS" 

	version("0.1.0", md5="d6d957c1398550abd709e9fba6ddf220")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-brglm2", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
