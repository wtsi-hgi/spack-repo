# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REselect(RPackage):
	"""Adaptive Clinical Trial Designs with Endpoint Selection and
Sample Size Reassessment

	Endpoint selection and sample size reassessment for multiple binary endpoints based on blinded and/or unblinded data. Trial design that allows an adaptive modification of the primary endpoint based on blinded information obtained at an interim analysis. The decision rule chooses the endpoint with the lower estimated required sample size. Additionally, the sample size is reassessed using the estimated event probabilities and correlation between endpoints. The implemented design is proposed in Bofill Roig, M., Gómez Melis, G., Posch, M., and Koenig, F. (2022). <doi:10.48550/arXiv.2206.09639>.
	"""
	
	cran = "eselect" 

	version("1.1", md5="4c216708b84d9dcb295d5ac8d6e130d6")

	depends_on("r-comparedesign", type=("build", "run"))
