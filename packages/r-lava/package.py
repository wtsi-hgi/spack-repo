# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLava(RPackage):
	"""Latent Variable Models.

	A general implementation of Structural Equation Models with latent
	variables (MLE, 2SLS, and composite likelihood estimators) with both
	continuous, censored, and ordinal outcomes (Holst and Budtz-Joergensen
	(2013) <doi:10.1007/s00180-012-0344-y>). Mixture latent variable models and
	non-linear latent variable models (Holst and Budtz-Joergensen (2019)
	<doi:10.1093/biostatistics/kxy082>). The package also provides methods for
	graph exploration (d-separation, back-door criterion), simulation of
	general non-linear latent variable models, and estimation of influence
	functions for a broad range of statistical models."""

	cran = "lava"

	license("GPL-3.0-only")

	version("1.8.0", md5="3e67327f96b08caeac828871968a4f8b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
