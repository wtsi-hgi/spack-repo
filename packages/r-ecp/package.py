# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcp(RPackage):
	"""Non-Parametric Multiple Change-Point Analysis of MultivariateData.

	Implements various procedures for finding multiple change-points from
	Matteson D. et al (2013) <doi:10.1080/01621459.2013.849605>, Zhang W. et al
	(2017) <doi:10.1109/ICDMW.2017.44>, Arlot S. et al (2019). Two methods make
	use of dynamic programming and pruning, with no distributional assumptions
	other than the existence of certain absolute moments in one method.
	Hierarchical and exact search methods are included. All methods return the
	set of estimated change-points as well as other summary information."""

	cran = "ecp"

	license("GPL-2.0-or-later")

	version("3.1.5", md5="e49b620d484f772fd2ccb59e652fb3f6")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
