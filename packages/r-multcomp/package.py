# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultcomp(RPackage):
	"""Simultaneous Inference in General Parametric Models.

	Simultaneous tests and confidence intervals for general linear hypotheses
	in parametric models, including linear, generalized linear, linear mixed
	effects, and survival models. The package includes demos reproducing
	analyzes presented in the book "Multiple Comparisons Using R" (Bretz,
	Hothorn, Westfall, 2010, CRC Press)."""

	cran = "multcomp"

	version("1.4-25", md5="b14e77316815f6f1d84e144fe32b6c26")

	depends_on("r-mvtnorm@1.0.10:", type=("build", "run"))
	depends_on("r-survival@2.39.4:", type=("build", "run"))
	depends_on("r-th-data@1.0.2:", type=("build", "run"))
	depends_on("r-sandwich@2.3.0:", type=("build", "run"))
	depends_on("r-codetools", type=("build", "run"))
