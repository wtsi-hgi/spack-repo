# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRospca(RPackage):
	"""Robust Sparse PCA using the ROSPCA Algorithm

	Implementation of robust sparse PCA using the ROSPCA algorithm 
             of Hubert et al. (2016) <DOI:10.1080/00401706.2015.1093962>.
	"""
	
	homepage = "https://github.com/TReynkens/rospca"
	cran = "rospca" 

	version("1.1.0", md5="2e4844b75f7b828731922df235b1fc1f")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-mrfdepth@1.0.5:", type=("build", "run"))
	depends_on("r-robustbase@0.92.6:", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-elasticnet", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
