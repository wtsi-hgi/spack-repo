# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMkpower(RPackage):
	"""Power Analysis and Sample Size Calculation

	Power analysis and sample size calculation for Welch and Hsu (Hedderich and Sachs (2018), ISBN:978-3-662-56657-2) t-tests including Monte-Carlo simulations of empirical power and type-I-error. Power and sample size calculation for Wilcoxon rank sum and signed rank tests via Monte-Carlo simulations. Power and sample size required for the evaluation of a diagnostic test(-system) (Flahault et al. (2005), <doi:10.1016/j.jclinepi.2004.12.009>; Dobbin and Simon (2007), <doi:10.1093/biostatistics/kxj036>) as well as for a single proportion (Fleiss et al. (2003), ISBN:978-0-471-52629-2; Piegorsch (2004), <doi:10.1016/j.csda.2003.10.002>; Thulin (2014), <doi:10.1214/14-ejs909>), comparing two negative binomial rates (Zhu and Lakkis (2014), <doi:10.1002/sim.5947>), and ANCOVA (Shieh (2020), <doi:10.1007/s11336-019-09692-3>).
	"""
	
	homepage = "https://github.com/stamats/MKpower"
	cran = "MKpower" 

	version("0.7", md5="55bcc18683243c9cbebb1f1f3ea8b436")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrixtests@0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mkdescr", type=("build", "run"))
	depends_on("r-mkinfer@0.4:", type=("build", "run"))
	depends_on("r-qqplotr", type=("build", "run"))
	depends_on("r-coin", type=("build", "run"))
