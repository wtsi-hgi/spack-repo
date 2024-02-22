# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNtlkwiex(RPackage):
	"""Computation of NTLKwIEx Distribution Properties

	Implements statistical tools for analyzing, simulating, and computing properties of the New Topp-Leone Kumaraswamy Inverse Exponential (NTLKwIEx) distribution. See Atchadé M, Otodji T, and Djibril A (2024) <doi:10.1063/5.0179458> and Atchadé M, Otodji T, Djibril A, and N'bouké M (2023) <doi:10.1515/phys-2023-0151> for details.
	"""
	
	cran = "NTLKwIEx" 

	version("0.1.0", md5="ac9949f7bc7ce160842e3ff9b32a7f15")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
