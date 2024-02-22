# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompositions(RPackage):
	"""Compositional Data Analysis.

	Provides functions for the consistent analysis of compositional  data (e.g.
	portions of substances) and positive numbers (e.g. concentrations)  in the
	way proposed by J. Aitchison and V. Pawlowsky-Glahn."""

	cran = "compositions"

	version("2.0-8", md5="114a1d48facb636b935ed812038584db")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-tensora", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-bayesm", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
