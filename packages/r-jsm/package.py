# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsm(RPackage):
	"""Semiparametric Joint Modeling of Survival and Longitudinal Data

	Maximum likelihood estimation for the semiparametric joint modeling of survival and longitudinal data. Refer to the Journal of Statistical Software article: <doi:10.18637/jss.v093.i02>.
	"""
	
	cran = "JSM" 

	version("1.0.1", md5="f53d664d40603ce371439bbbd6c9aa67")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
