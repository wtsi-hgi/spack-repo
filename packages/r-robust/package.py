# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
# See the Spack documentation for more information on packaging.

from spack.package import *


class RRobust(RPackage):
	"""Port of the S+ Robust Library.

	Methods for robust statistics, a state of the art in the early 2000s,
	notably for robust regression and robust multivariate analysis."""

	cran = "robust"

	version("0.7-4", md5="d3d9bfda8c6ba50021269d5924252430")

	depends_on("r-fit-models", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
