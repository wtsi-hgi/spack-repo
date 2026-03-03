# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrtcs(RPackage):
	"""Randomized Response Techniques for Complex Surveys

	Point and interval estimation of linear parameters with data
    obtained from complex surveys (including stratified and clustered samples)
    when randomization techniques are used. The randomized response technique
    was developed to obtain estimates that are more valid when studying
    sensitive topics. Estimators and variances for 14 randomized response
    methods for qualitative variables and 7 randomized response methods for
    quantitative variables are also implemented. In addition, some data sets
    from surveys with these randomization methods are included in the package.
	"""
	
	cran = "RRTCS" 

	version("0.0.4", md5="a720427b0057a11c987a13f4df8c113b")

	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-samplingvarest", type=("build", "run"))
