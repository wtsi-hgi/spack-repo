# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLuminescence(RPackage):
	"""Comprehensive Luminescence Dating Data Analysis

	A collection of various R functions for the purpose of Luminescence
    dating data analysis. This includes, amongst others, data import, export,
    application of age models, curve deconvolution, sequence analysis and
    plotting of equivalent dose distributions.
	"""
	
	homepage = "https://CRAN.R-project.org/package=Luminescence"
	cran = "Luminescence" 

	version("0.9.23", md5="8cf2292ea6f1f103ea7527e96d7e7e7e")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-bbmle@1.0.25:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-deoptim@2.2.8:", type=("build", "run"))
	depends_on("r-httr@1.4.7:", type=("build", "run"))
	depends_on("r-interp@1.1.4:", type=("build", "run"))
	depends_on("r-lamw@2.2.1:", type=("build", "run"))
	depends_on("r-matrixstats@1:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.4:", type=("build", "run"))
	depends_on("r-mclust@6:", type=("build", "run"))
	depends_on("r-readxl@1.4.3:", type=("build", "run"))
	depends_on("r-rcpp@1.0.11:", type=("build", "run"))
	depends_on("r-shape@1.4.6:", type=("build", "run"))
	depends_on("r-xml@3.99.0.15:", type=("build", "run"))
	depends_on("r-zoo@1.8.12:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.12.6.6:", type=("build", "run"))
