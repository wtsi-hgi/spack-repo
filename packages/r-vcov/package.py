# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVcov(RPackage):
	"""Variance-Covariance Matrices and Standard Errors

	Methods for faster extraction (about 5x faster in a few test cases) of variance-covariance matrices and standard errors from models. Methods in the 'stats' package tend to rely on the summary method, which may waste time computing other summary statistics which are summarily ignored.
	"""
	
	homepage = "https://github.com/MichaelChirico/vcov"
	cran = "vcov" 

	version("0.0.1", md5="752d9852d0ef6b3608cd21befa547526")

	depends_on("r@3.4:", type=("build", "run"))
