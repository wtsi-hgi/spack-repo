# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJomo(RPackage):
	"""Multilevel Joint Modelling Multiple Imputation.

	Similarly to Schafer's package 'pan', 'jomo' is a package for multilevel
	joint modelling multiple imputation (Carpenter and Kenward, 2013)
	<doi:10.1002/9781119942283>. Novel aspects of 'jomo' are the possibility of
	handling binary and categorical data through latent normal variables, the
	option to use cluster-specific covariance matrices and to impute compatibly
	with the substantive model."""

	cran = "jomo"

	license("GPL-2.0-only")

	version("2.7-6", md5="473d277969676494a6df604b477809e9")

	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ordinal", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
