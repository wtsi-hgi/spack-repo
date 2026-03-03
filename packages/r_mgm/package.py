# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgm(RPackage):
	"""Estimating Time-Varying k-Order Mixed Graphical Models

	Estimation of k-Order time-varying Mixed Graphical Models and mixed VAR(p) models via elastic-net regularized neighborhood regression. For details see Haslbeck & Waldorp (2020) <doi:10.18637/jss.v093.i08>.
	"""
	
	homepage = "https://www.jstatsoft.org/article/view/v093i08"
	cran = "mgm" 

	version("1.2-14", md5="153028b85da8ceafb4bfaaf3c7fa410f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
