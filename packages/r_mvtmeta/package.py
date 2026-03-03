# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvtmeta(RPackage):
	"""Multivariate Meta-Analysis

	Functions to run fixed effects or random effects multivariate meta-analysis.
	"""
	
	cran = "mvtmeta" 

	version("1.1", md5="cbdf46db7dede995ef39d7c0a4e21a1e")

	depends_on("r-gtools", type=("build", "run"))
