# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunstattest(RPackage):
	"""Statistical Testing for Functional Data

	Implementation of two sample comparison procedures based on median-based statistical tests 
    for functional data, introduced in Smida et al (2022) <doi:10.1080/10485252.2022.2064997>. 
    Other competitive state-of-the-art approaches proposed by Chakraborty and Chaudhuri (2015) <doi:10.1093/biomet/asu072>,
    Horvath et al (2013) <doi:10.1111/j.1467-9868.2012.01032.x> or Cuevas et al (2004) <doi:10.1016/j.csda.2003.10.021>
    are also included in the package, as well as procedures to run test result comparisons and power analysis 
    using simulations.
	"""
	
	homepage = "https://plmlab.math.cnrs.fr/gdurif/funStatTest/"
	cran = "funStatTest" 

	version("1.0.2", md5="b0b41b47a9f7280bac7e077f73a60327")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
