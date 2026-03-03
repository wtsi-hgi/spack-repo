# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbent(RPackage):
	"""Robust Bent Line Regression

	An implementation of robust bent line regression. It can fit the bent line regression and test the existence of change point,
    for the paper, "Feipeng Zhang and Qunhua Li (2016). Robust bent line regression, submitted."
	"""
	
	homepage = "http://arxiv.org/abs/1606.02234"
	cran = "Rbent" 

	version("0.1.0", md5="33bf035fc11e268c6dac38ebfe5fafe9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rfit", type=("build", "run"))
