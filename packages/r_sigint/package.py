# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSigint(RPackage):
	"""Estimate the Parameters of a Discrete Crisis-Bargaining Game

	Provides pseudo-likelihood methods for empirically analyzing common signaling games in international relations as described in Crisman-Cox and Gibilisco (2019) <doi:10.1017/psrm.2019.58>.
	"""
	
	homepage = "https://github.com/ccrismancox/sigint"
	cran = "sigInt" 

	version("0.2.0", md5="2e78c1142781fda37b607f964bde481e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
