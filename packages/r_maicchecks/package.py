# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaicchecks(RPackage):
	"""Assessing the Numerical Feasibility for Conducting a
Matching-Adjusted Indirect Comparison (MAIC)

	A collection of easy-to-implement tools for checking whether a MAIC can be conducted. An alternative way of calculating weights is also included. These methods are introduced in Glimm & Yau (2021) <arXiv:2108.01896>.
	"""
	
	cran = "maicChecks" 

	version("0.1.2", md5="0217ec8a3bee3c7525eea4418907f37b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
