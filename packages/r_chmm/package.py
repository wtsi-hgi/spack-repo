# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChmm(RPackage):
	"""Coupled Hidden Markov Models

	An exact and a variational inference for
    coupled Hidden Markov Models applied to the joint detection of copy number variations.
	"""
	
	homepage = "http://github.com/julieaubert/CHMM"
	cran = "CHMM" 

	version("0.1.1", md5="5654524d3378268614aab4e61de48399")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
