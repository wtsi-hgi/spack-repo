# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhmle(RPackage):
	"""Methods for the Additive Hazard Model

	Methods for fitting additive hazards model.
			 Perform the maximum likelihood method as well as the traditional Aalen's method for estimating the additive hazards model. 
			 For details see Chengyuan Lu(2021) <arXiv:2004.06156>. 
	"""
	
	cran = "ahMLE"

	version("1.20.1", md5="6243dddac564f76112922b253f1088ed")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-invgauss", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
