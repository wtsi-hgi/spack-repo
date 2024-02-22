# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepgmm(RPackage):
	"""Deep Gaussian Mixture Models

	Deep Gaussian mixture models as proposed by Viroli and McLachlan (2019) 
    <doi:10.1007/s11222-017-9793-z> provide a generalization of classical Gaussian mixtures 
    to multiple layers. Each layer contains a set of latent variables that follow a mixture of 
    Gaussian distributions. To avoid overparameterized solutions, dimension reduction is 
    applied at each layer by way of factor models.
	"""
	
	homepage = "https://github.com/suren-rathnayake/deepgmm"
	cran = "deepgmm" 

	version("0.2.1", md5="738ea23f6a95c7382ddfc327cf0ab91b")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
