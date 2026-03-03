# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDssp(RPackage):
	"""Implementation of the Direct Sampling Spatial Prior

	Draw samples from the direct sampling spatial prior model as
    described in G. White, D. Sun, P. Speckman (2019) <arXiv:1906.05575>. The basic model assumes a Gaussian
    likelihood and derives a spatial prior based on thin-plate splines.
	"""
	
	homepage = "https://github.com/gentrywhite/DSSP"
	cran = "DSSP" 

	version("0.1.1", md5="ddfbd7266eec15b993006245179628c8")

	depends_on("r-mcmcse", type=("build", "run"))
	depends_on("r-posterior", type=("build", "run"))
	depends_on("r-rust", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
