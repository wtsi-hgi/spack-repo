# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTlcar(RPackage):
	"""Computation of Topp-Leone Cauchy Rayleigh (TLCAR )
distribution's properties

	Provides a comprehensive suite of statistical tools for analyzing, simulating, and computing properties of the Topp-Leone Cauchy Rayleigh (TLCAR) distribution, a versatile distribution amalgamating features of the Topp-Leone, Cauchy, and Rayleigh distributions, ideal for modeling intricate, heterogeneous data across scientific domains. See Atchadé, M.N., Bogninou, M.J., and Djibril, A.M. (2023) <doi:10.1007/s44199-023-00066-4> and Atchadé, M.N., Bogninou, M.J., and Djibril, A.M. (2024) <doi:10.1007/s44199-023-00069-1> for further insights.
	"""
	
	cran = "TLCAR" 

	version("0.1.0", md5="54d1ca1bbd0e6a3dc1b31fcd7c2f632d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
