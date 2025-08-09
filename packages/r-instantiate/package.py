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

	version("0.2.3", sha256="dff964c58ca82684cfe0f9fcbe3cee683294329cdc42e83a1ecdf0121b40cdd7")
	version("0.2.2", sha256="a20de42dac76cddf234728be969a651ff6096ffbdb23f1ff2a75fd094116bd5a")
	version("0.2.1", sha256="24016f73cba073b4c23620b46def6b265068113aedfb7a0d531a7b583c5c7e71")
	version("0.2.0", sha256="d084510cf42e284d9a7e113693b2db32cd0bed0061918d356d5eab3f22ef1823")
	version("0.0.2", sha256="1f6323bca47180cd158d10b3ebc9eab11eddbc60c7edaa19442ce359a516cee2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
