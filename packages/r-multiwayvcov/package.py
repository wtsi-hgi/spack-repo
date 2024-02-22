# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiwayvcov(RPackage):
	"""Multi-Way Standard Error Clustering

	Exports two functions implementing
    multi-way clustering using the method suggested by Cameron, Gelbach, &
    Miller (2011) and cluster (or block)
    bootstrapping for estimating variance-covariance matrices. Normal one and
    two-way clustering matches the results of other common statistical
    packages.  Missing values are handled transparently and rudimentary
    parallelization support is provided.
	"""
	
	homepage = "http://sites.google.com/site/npgraham1/research/code"
	cran = "multiwayvcov" 

	version("1.2.3", md5="dcd9c19ebe95138fc59c7c6d64da9db5")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
