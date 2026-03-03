# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgms(RPackage):
	"""Bayesian Analysis of Networks of Binary and/or Ordinal Variables

	Bayesian variable selection methods for analyzing the structure of a Markov Random Field model for a network of binary and/or ordinal variables. Details of the implemented methods can be found in: Marsman and Haslbeck (2023) <doi:10.31234/osf.io/ukwrf>.
	"""
	
	homepage = "https://maartenmarsman.github.io/bgms/"
	cran = "bgms" 

	version("0.1.3", md5="cfb8ecbab4249aa0317c246f673ac9fe")
	version("0.1.2", md5="7e71dd526831341f105822b9518953fa")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
