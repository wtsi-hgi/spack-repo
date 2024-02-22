# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAltr2(RPackage):
	"""Alternative Estimators to Adjusted R-Squared

	Provides alternatives to the normal adjusted R-squared estimator for the estimation of the multiple squared correlation in regression models, 
              as fitted by the lm() function. The alternative estimators are described in Karch (2016) <DOI:10.31234/osf.io/v8dz5>.
	"""
	
	homepage = "https://github.com/karchjd/altR2"
	cran = "altR2" 

	version("1.0.0", md5="62bc567339c8c63d3c6e0ccc8710a763", url="https://cran.r-project.org/src/contrib/altR2_1.0.0.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-gsl@1.9.10.3:", type=("build", "run"))
	depends_on("r-purrr@0.3.2:", type=("build", "run"))
