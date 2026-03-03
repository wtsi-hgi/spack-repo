# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsmd(RPackage):
	"""Bayes Screening and Model Discrimination

	Bayes screening and model discrimination follow-up designs.
	"""
	
	cran = "BsMD" 

	version("2023.920", md5="ef249f21e72cd49011a88f3d12a0d5b9")

	depends_on("r@4:", type=("build", "run"))
