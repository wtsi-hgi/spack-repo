# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMorpheus(RPackage):
	"""Estimate Parameters of Mixtures of Logistic Regressions

	Mixture of logistic regressions parameters (H)estimation with
    (U)spectral methods. The main methods take d-dimensional inputs and a vector
    of binary outputs, and return parameters according to the GLMs mixture model
    (General Linear Model). For more details see chapter 3 in the PhD thesis of
		Mor-Absa Loum: <https://www.theses.fr/s156435>, available here
		<https://theses.hal.science/tel-01877796/document>.
	"""
	
	homepage = "https://github.com/yagu0/morpheus"
	cran = "morpheus" 

	version("1.0-4", md5="1ad74b7d7640bab1cf67955508798e13")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-jointdiag", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
