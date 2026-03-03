# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFeaturizer(RPackage):
	"""Some Helper Functions that Help Create Features from Data

	A collection of functions that would help one to build features based on external data. Very useful for Data Scientists in data to day work. Many functions create features using parallel computation. Since the nitty gritty of parallel computation is hidden under the hood, the user need not worry about creating clusters and shutting them down.
	"""
	
	cran = "featurizer" 

	version("0.2", md5="0dd63854a48ac04b6bbc5538fe5e4d34")

	depends_on("r@3.2.1:", type=("build", "run"))
