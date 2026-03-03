# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlcm(RPackage):
	"""Sparse Latent Class Model for Cognitive Diagnosis

	Perform a Bayesian estimation of the exploratory 
    Sparse Latent Class Model for Binary Data 
    described by Chen, Y., Culpepper, S. A., and Liang, F. (2020) 
    <doi:10.1007/s11336-019-09693-2>.
	"""
	
	homepage = "https://github.com/tmsalab/slcm"
	cran = "slcm" 

	version("0.1.0", md5="95b7831395da2ccc58733f82a7d2df79")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
