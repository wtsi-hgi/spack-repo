# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPanprsnext(RPackage):
	"""Building PRS Models Based on Summary Statistics of GWAs

	Shrinkage estimator for polygenic risk prediction (PRS) models based on summary statistics of genome-wide association (GWA) studies. Based upon the methods and original 'PANPRS' package as found in: Chen, Chatterjee, Landi, and Shi (2020) <doi:10.1080/01621459.2020.1764849>.
	"""
	
	cran = "PANPRSnext" 

	version("1.2.0", md5="8960963c9b97fb455c8503b944267cc7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
