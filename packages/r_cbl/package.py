# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbl(RPackage):
	"""Causal Discovery under a Confounder Blanket

	Methods for learning causal relationships among a set of
    foreground variables X based on signals from a (potentially much
    larger) set of background variables Z, which are known non-descendants
    of X. The confounder blanket learner (CBL) uses sparse regression
    techniques to simultaneously perform many conditional independence
    tests, with complementary pairs stability selection to guarantee
    finite sample error control. CBL is sound and complete with respect to
    a so-called "lazy oracle", and works with both linear and nonlinear
    systems. For details, see Watson & Silva (2022) <arXiv:2205.05715>.
	"""
	
	homepage = "https://github.com/dswatson/cbl"
	cran = "cbl" 

	version("0.1.3", md5="c4109c38d193bceafafc8f22fa7f684f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-lightgbm", type=("build", "run"))
