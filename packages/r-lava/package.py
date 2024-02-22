# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
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

	version("1.7.3", md5="de13698031fad1ecaa5d5d451d45a5f1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
