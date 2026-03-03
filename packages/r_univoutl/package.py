# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnivoutl(RPackage):
	"""Detection of Univariate Outliers

	Well known outlier detection techniques in the univariate case. Methods to deal with skewed distribution are included too. The Hidiroglou-Berthelot (1986) method to search for outliers in ratios of historical data is implemented as well. When available, survey weights can be used in outliers detection.
	"""
	
	homepage = "https://github.com/marcellodo/univOutl"
	cran = "univOutl" 

	version("0.4", md5="fea4abe59953f3808ddd3545c25f6e0d")

	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
