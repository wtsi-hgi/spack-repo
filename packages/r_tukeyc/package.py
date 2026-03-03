# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTukeyc(RPackage):
	"""Conventional Tukey Test

	Perform the conventional Tukey test from formula, 
             lm, aov, aovlist and lmer objects.
	"""
	
	homepage = "https://github.com/jcfaria/TukeyC"
	cran = "TukeyC" 

	version("1.3-42", md5="6d09af2a1cd688858d6ce2e46efbf5d0")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-doby", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
