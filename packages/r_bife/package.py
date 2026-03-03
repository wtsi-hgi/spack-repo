# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBife(RPackage):
	"""Binary Choice Models with Fixed Effects

	Estimates fixed effects binary choice models (logit and probit) with potentially many
  individual fixed effects and computes average partial effects. Incidental parameter bias can be
  reduced with an asymptotic bias correction proposed by Fernandez-Val (2009)
  <doi:10.1016/j.jeconom.2009.02.007>.
	"""
	
	homepage = "https://github.com/amrei-stammann/bife"
	cran = "bife" 

	version("0.7.2", md5="3b6655a653ad346d4f16a6e5e3aeb0fc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
