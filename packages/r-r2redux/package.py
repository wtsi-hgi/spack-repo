# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2redux(RPackage):
	"""R2 Statistic

	R2 statistic for significance test. Variance and covariance of R2 values used to assess the 95% CI and p-value of the R2 difference.
	"""
	
	homepage = "https://github.com/mommy003/r2redux"
	cran = "r2redux" 

	version("1.0.17", md5="b29d5420418206b39ba157e48313f34b")

	depends_on("r@2.10:", type=("build", "run"))
