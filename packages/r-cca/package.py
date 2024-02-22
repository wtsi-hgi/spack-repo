# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RCca(RPackage):
	"""Canonical Correlation Analysis.

	Provides a set of functions that extend the 'cancor' function with new
	numerical and graphical outputs. It also include a regularized extension of
	the canonical correlation analysis to deal with datasets with more
	variables than observations."""

	cran = "CCA"

	version("1.2.2", md5="08e6d3e50ce1668c516134e220d25df7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
