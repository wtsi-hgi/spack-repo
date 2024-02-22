# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpwbs(RPackage):
	"""Nonparametric Multiple Change Point Detection Using WBS

	Implements the procedure from G. J. Ross (2021) - "Nonparametric Detection of Multiple Location-Scale Change Points via Wild Binary Segmentation" <arxiv:2107.01742>. This uses a version of Wild Binary Segmentation to detect multiple location-scale (i.e. mean and/or variance) change points in a sequence of univariate observations, with a strict control on the probability of incorrectly detecting a change point in a sequence which does not contain any.
	"""
	
	cran = "npwbs" 

	version("0.2.0", md5="a029ab91de5e1194311e210e9a85d0cf")

	depends_on("r@3.6:", type=("build", "run"))
