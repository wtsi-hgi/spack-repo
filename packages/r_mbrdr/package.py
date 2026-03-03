# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbrdr(RPackage):
	"""Model-Based Response Dimension Reduction

	Functions for model-based response dimension reduction. Usual dimension reduction methods in multivariate regression focus on the reduction of predictors, not responses.  The response dimension reduction is theoretically founded in Yoo and Cook (2008) <doi:10.1016/j.csda.2008.07.029>. Later, three model-based response dimension reduction approaches are proposed in Yoo (2016) <doi:10.1080/02331888.2017.1410152> and Yoo (2019) <doi:10.1016/j.jkss.2019.02.001>. The method by Yoo and Cook (2008) is based on non-parametric ordinary least squares, but the model-based approaches are done through maximum likelihood estimation. For two model-based response dimension reduction methods called principal fitted response reduction and unstructured principal fitted response reduction, chi-squared tests are provided for determining the dimension of the response subspace.
	"""
	
	cran = "mbrdr" 

	version("1.1.1", md5="3e0e14953c3530f873f99f7a6f680d7c")

	depends_on("r@3.5:", type=("build", "run"))
