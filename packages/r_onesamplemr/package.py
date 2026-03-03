# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnesamplemr(RPackage):
	"""One Sample Mendelian Randomization and Instrumental Variable
Analyses

	Useful functions for one-sample (individual level data)
    Mendelian randomization and instrumental variable analyses. The
    package includes implementations of; the Sanderson and Windmeijer
    (2016) <doi:10.1016/j.jeconom.2015.06.004> conditional F-statistic,
    the multiplicative structural mean model Hernán and Robins (2006)
    <doi:10.1097/01.ede.0000222409.00878.37>, and two-stage predictor
    substitution and two-stage residual inclusion estimators explained by
    Terza et al. (2008) <doi:10.1016/j.jhealeco.2007.09.009>.
	"""
	
	homepage = "https://github.com/remlapmot/OneSampleMR"
	cran = "OneSampleMR" 

	version("0.1.3", md5="efe2ad53a482eb9dc42d1cfe6ccd5903")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-gmm", type=("build", "run"))
	depends_on("r-ivreg", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
