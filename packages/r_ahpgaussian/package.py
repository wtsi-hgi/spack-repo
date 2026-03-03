# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhpgaussian(RPackage):
	"""New Multicriteria Method: AHPGaussian

	Implements the Analytic Hierarchy Process (AHP) method using Gaussian normalization (AHPGaussian) to derive the relative weights of the criteria and alternatives. It also includes functions for visualizing the results and generating graphical outputs. Method as described in: dos Santos, Marcos (2021) <doi:10.13033/ijahp.v13i1.833>.
	"""
	
	cran = "AHPGaussian" 

	version("0.1.1", md5="d46f5eda795c91732d642541f31da207")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
