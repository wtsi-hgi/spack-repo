# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForplo(RPackage):
	"""Flexible Forest Plots

	Simplifies the creation and customization of forest plots (alternatively called dot-and-whisker plots). Input classes accepted by 'forplo' are data.frame, matrix, lm, glm, and coxph. 'forplo' was written in base R and does not depend on other packages.
	"""
	
	cran = "forplo" 

	version("0.2.5", md5="bd3850dd4e605ba309995d5e840283ec")

	depends_on("r@3.5:", type=("build", "run"))
