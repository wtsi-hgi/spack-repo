# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvival(RPackage):
	"""Survival Analysis.

	Contains the core survival analysis routines, including definition of Surv
	objects, Kaplan-Meier and Aalen-Johansen (multi-state) curves, Cox models,
	and parametric accelerated failure time models."""

	cran = "survival"

	version("3.5-8", md5="1c09fd690cd4392bb0adb7f0e2c7fe58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
