# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLpme(RPackage):
	"""Nonparametric Estimation of Measurement Error Models

	Provide nonparametric methods for mean regression model, modal regression and conditional density estimation in the presence/absence of measurement error. Bandwidth selection is also provided for each method. See Huang and Zhou (2017) <doi:10.1080/10485252.2017.1303060>, Zhou and Huang (2016) <doi:10.1214/16-EJS1210>, Huang and Zhou (2020) <doi:10.1214/20-EJS1688>, and Zhou and Huang (2019) <doi:10.1080/03610918.2017.1402044>.
	"""
	
	cran = "lpme" 

	version("1.1.3", md5="1abe9b9b4e96b0aab03efa29f8d18389")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-decon", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-locpol", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.4.300:", type=("build", "run"))
