# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedigreemm(RPackage):
	"""Pedigree-Based Mixed-Effects Models

	Fit pedigree-based mixed-effects models.
	"""
	
	homepage = "https://github.com/anainesvs/pedigreemm/"
	cran = "pedigreemm" 

	version("0.3-4", md5="9d290a09481c49a39e75d8d9a3586409")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lme4@1:", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
