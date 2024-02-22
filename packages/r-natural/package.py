# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNatural(RPackage):
	"""Estimating the Error Variance in a High-Dimensional Linear Model

	Implementation of the two error variance estimation methods in high-dimensional linear models of Yu, Bien (2017) <arXiv:1712.02412>.
	"""
	
	homepage = "https://arxiv.org/abs/1712.02412"
	cran = "natural" 

	version("0.9.0", md5="bbce7f78a4a2040eb2ea71daf27732df")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
