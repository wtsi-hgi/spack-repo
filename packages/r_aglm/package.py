# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAglm(RPackage):
	"""Accurate Generalized Linear Model

	Provides functions to fit Accurate Generalized Linear Model (AGLM) models, visualize them, and predict for new data. AGLM is defined as a regularized GLM which applies a sort of feature transformations using a discretization of numerical features and specific coding methodologies of dummy variables. For more information on AGLM, see Suguru Fujita, Toyoto Tanaka, Kenji Kondo and Hirokazu Iwasawa (2020) <https://www.institutdesactuaires.com/global/gene/link.php?doc_id=16273&fg=1>.
	"""
	
	homepage = "https://github.com/kkondo1981/aglm"
	cran = "aglm" 

	version("0.4.0", md5="e2ad7fdb3bbd888bc26e85d1d2452ea9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-glmnet@4.0.2:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
