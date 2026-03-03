# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElasticnet(RPackage):
	"""Elastic-Net for Sparse Estimation and Sparse PCA

	Provides functions for fitting the entire
        solution path of the Elastic-Net and also provides functions
        for doing sparse PCA.  
	"""
	
	homepage = "http://users.stat.umn.edu/~zouxx019/"
	cran = "elasticnet" 

	version("1.3", md5="6cbe6a3a3828656bc331b2f0181a3ca1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
