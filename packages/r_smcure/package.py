# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmcure(RPackage):
	"""Fit Semiparametric Mixture Cure Models

	An R-package for Estimating Semiparametric PH and AFT Mixture Cure Models.
	"""
	
	cran = "smcure" 

	version("2.1", md5="af7f2bcbc3030fc36fa05884a747b27f")

	depends_on("r-survival", type=("build", "run"))
