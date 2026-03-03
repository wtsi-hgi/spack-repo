# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDifnlr(RPackage):
	"""DIF and DDF Detection by Non-Linear Regression Models

	Detection of differential item functioning (DIF) among dichotomously scored items and differential distractor functioning (DDF) among unscored items with non-linear regression  procedures based on generalized logistic regression models (Hladka & Martinkova, 2020, <doi:10.32614/RJ-2020-014>).
	"""
	
	cran = "difNLR" 

	version("1.4.2-1", md5="c739340306fea3cae7dd2175aba0dcd9")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-calculus", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
