# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTwophaseind(RPackage):
	"""Estimate Gene-Treatment Interaction Exploiting Randomization

	Estimation of gene-treatment interactions in randomized clinical trials exploiting gene-treatment independence. Methods used in the package refer to J. Y. Dai, M. LeBlanc, and C. Kooperberg (2009) Biometrics <doi:10.1111/j.1541-0420.2008.01046.x>.
	"""
	
	cran = "TwoPhaseInd" 

	version("1.1.2", md5="b7b280cd180ab0110e78a86067e4e64f")

	depends_on("r-survival", type=("build", "run"))
