# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcc(RPackage):
	"""Facilitating Estimation of the Intraclass Correlation
Coefficient

	Assist in the estimation of the Intraclass Correlation Coefficient
    (ICC) from variance components of a one-way analysis of variance and also
    estimate the number of individuals or groups necessary to obtain an ICC
    estimate with a desired confidence interval width.
	"""
	
	homepage = "https://github.com/matthewwolak/ICC"
	cran = "ICC" 

	version("2.4.0", md5="c7d6a7ff7b16b761db590d0cbf52b973")

