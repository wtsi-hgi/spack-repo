# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultordrs(RPackage):
	"""Model Multivariate Ordinal Responses Including Response Styles

	In the case of multivariate ordinal responses, parameter estimates can be severely biased if personal response styles are ignored. This packages provides methods to account for personal response styles and to explain the effects of covariates on the response style, as proposed by Schauberger and Tutz 2021 <doi:10.1177/1471082X20978034>. The method is implemented both for the multivariate cumulative model and the multivariate adjacent categories model.
	"""
	
	cran = "MultOrdRS" 

	version("0.1-3", md5="9782aa0fd86676e496d98309f96e4ac7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-statmod", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
