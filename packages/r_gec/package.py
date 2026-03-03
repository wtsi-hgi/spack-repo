# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGec(RPackage):
	"""Generalized Exponentiated Composite Distributions

	Contains the framework of the estimation, sampling, and hypotheses testing for two special distributions (Exponentiated Exponential-Pareto and Exponentiated Inverse Gamma-Pareto) within the family of Generalized Exponentiated Composite distributions. The detailed explanation and the applications of these two distributions were introduced in Bowen Liu, Malwane M.A. Ananda (2022) <doi:10.1080/03610926.2022.2050399>, Bowen Liu, Malwane M.A. Ananda (2022) <doi:10.3390/math10111895>, and Bowen Liu, Malwane M.A. Ananda (2022) <doi:10.3390/app13010645>. 
	"""
	
	cran = "GEC" 

	version("0.1.0", md5="6e5ccac1da1919144ce7c1cddd7531a2")

	depends_on("r-mistr", type=("build", "run"))
