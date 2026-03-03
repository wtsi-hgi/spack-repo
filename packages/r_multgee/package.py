# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultgee(RPackage):
	"""GEE Solver for Correlated Nominal or Ordinal Multinomial
Responses

	GEE solver for correlated nominal or ordinal multinomial responses
    using a local odds ratios parameterization.
	"""
	
	homepage = "https://github.com/AnestisTouloumis/multgee"
	cran = "multgee" 

	version("1.9.0", md5="0ae6997017b356f7ab3abe7ca0c52a70")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-gnm", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
