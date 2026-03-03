# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeclim(RPackage):
	"""Numerical Calibration of Proxy-Climate Relationships

	Bootstrapped response and correlation functions,
    seasonal correlations and evaluation of reconstruction
    skills for use in dendroclimatology and dendroecology,
    see Zang and Biondi (2015) <doi:10.1111/ecog.01335>.
	"""
	
	homepage = "https://github.com/cszang/treeclim"
	cran = "treeclim" 

	version("2.0.6.0", md5="a6fb02fbc20767b9a006259ee31d620b")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-lmodel2", type=("build", "run"))
	depends_on("r-np", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.0.2:", type=("build", "run"))
