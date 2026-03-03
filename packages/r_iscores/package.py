# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIscores(RPackage):
	"""Proper Scoring Rules for Missing Value Imputation

	Implementation of a KL-based scoring rule to assess the quality of different missing value imputations in the broad sense as introduced in Michel et al. (2021)  <arXiv:2106.03742>.
	"""
	
	cran = "Iscores" 

	version("1.1.0", md5="6984f1d4de0cc8eda32c40e76df94245")

	depends_on("r-ranger", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
