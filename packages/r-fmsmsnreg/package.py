# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmsmsnreg(RPackage):
	"""Regression Models with Finite Mixtures of Skew Heavy-Tailed
Errors

	Fit linear regression models where the random errors follow a finite mixture of of Skew Heavy-Tailed Errors.
	"""
	
	cran = "FMsmsnReg" 

	version("1.0", md5="8fb9edac3cbc12275bb5f251c59fe227")

	depends_on("r-mvtnorm", type=("build", "run"))
