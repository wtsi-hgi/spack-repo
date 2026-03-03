# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVanquish(RPackage):
	"""Variant Quality Investigation Helper

	Imports Variant Calling Format file into R. It can detect
             whether a sample contains contaminant from the same species.
             In the first stage of the approach, a change-point detection
             method is used to identify copy number variations for filtering.
             Next, features are extracted from the data for a support vector
             machine model. For log-likelihood calculation, the deviation
             parameter is estimated by maximum likelihood method. Using
             a radial basis function kernel support vector machine, the
             contamination of a sample can be detected.
	"""
	
	cran = "vanquish" 

	version("1.0.0", md5="2120228d55327c70a5bad9a66f075262")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
