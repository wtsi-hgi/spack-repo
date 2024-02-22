# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcscopula(RPackage):
	"""Non-Central Squared Copula Models Estimation

	Inference and dependence measure for the non-central squared Gaussian, Student, Clayton, Gumbel, and Frank copula models.The description of the methodology is taken from Section 3 of Nasri, Remillard and Bouezmarni (2019) <doi:10.1016/j.jmva.2019.03.007>.
	"""
	
	cran = "NCSCopula" 

	version("1.0.1", md5="17e1493bcecc526c0b8ef95888a679f2")

	depends_on("r-copula", type=("build", "run"))
