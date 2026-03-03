# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmcluster(RPackage):
	"""EM Algorithm for Model-Based Clustering of Finite Mixture
Gaussian Distribution

	EM algorithms and several efficient
        initialization methods for model-based clustering of finite
        mixture Gaussian distribution with unstructured dispersion
        in both of unsupervised and semi-supervised learning.
	"""
	
	homepage = "https://github.com/snoweye/EMCluster"
	cran = "EMCluster" 

	version("0.2-15", md5="76306925a08b1dd20b25fda7e44b981a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
