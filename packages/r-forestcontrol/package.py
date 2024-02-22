# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForestcontrol(RPackage):
	"""Approximate False Positive Rate Control in Selection Frequency
for Random Forest

	Approximate false positive rate control in selection frequency for
    random forest using the methods described by Ender Konukoglu and Melanie Ganz (2014) <arXiv:1410.2838>.
    Methods for calculating the selection frequency threshold at false positive rates
    and selection frequency false positive rate feature selection.
	"""
	
	homepage = "https://github.com/aberHRML/forestControl"
	cran = "forestControl" 

	version("0.2.2", md5="322bd3caa1f036aef226fd4dc1c0a23a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
