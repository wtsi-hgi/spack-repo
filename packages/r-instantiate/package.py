# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInstantiate(RPackage):
	"""Pre-Compiled 'CmdStan' Models in R Packages

	Similar to 'rstantools' for 'rstan',
  the 'instantiate' package builds pre-compiled
  'CmdStan' models into CRAN-ready statistical modeling R packages.
  The models compile once during installation,
  the executables live inside the file systems of their respective packages,
  and users have the full power and convenience of
  'cmdstanr' without any additional compilation after package installation.
  This approach saves time and helps R package developers
  migrate from 'rstan' to the more modern 'cmdstanr'.
  Packages 'rstantools', 'cmdstanr', 'stannis', and
  'stanapi' are similar Stan clients with different objectives.
	"""
	
	homepage = "https://wlandau.github.io/instantiate/"
	cran = "instantiate" 

	version("0.2.2", md5="87aea40edac97d736d89db9cb7c91635")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
