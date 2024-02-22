# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMda(RPackage):
	"""Mixture and Flexible Discriminant Analysis.

	Mixture and flexible discriminant analysis, multivariate adaptive
	regression splines (MARS), BRUTO."""

	cran = "mda"

	version("0.5-4", md5="d05782cc524a7c680211bfacdc799ad7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
