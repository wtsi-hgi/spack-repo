# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlme(RPackage):
	"""Linear and Nonlinear Mixed Effects Models.

	Fit and compare Gaussian linear and nonlinear mixed-effects models."""

	cran = "nlme"

	license("GPL-2.0-or-later")

	version("3.1-164", md5="51367d404f1ca2f395922b073a7180a3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
