# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMiceafter(RPackage):
	"""Data and Statistical Analyses after Multiple Imputation

	
   Statistical Analyses and Pooling after Multiple Imputation. A large variety 
   of repeated statistical analysis can be performed and finally pooled. Statistical analysis 
   that are available are, among others, Levene's test, Odds and Risk Ratios, One sample 
   proportions, difference between proportions and linear and logistic regression models. 
   Functions can also be used in combination with the Pipe operator. 
   More and more statistical analyses and pooling functions will be added over time.
   Heymans (2007) <doi:10.1186/1471-2288-7-33>.
   Eekhout (2017) <doi:10.1186/s12874-017-0404-7>.
	 Wiel (2009) <doi:10.1093/biostatistics/kxp011>.
	 Marshall (2009) <doi:10.1186/1471-2288-9-57>.
	 Sidi (2021) <doi:10.1080/00031305.2021.1898468>.
	 Lott (2018) <doi:10.1080/00031305.2018.1473796>.
	 Grund (2021) <doi:10.31234/osf.io/d459g>.
	"""
	
	homepage = "https://mwheymans.github.io/miceafter/"
	cran = "miceafter" 

	version("0.5.0", md5="d04658f57dc1cd775d38392297c2a5c4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-survival@3.1.12:", type=("build", "run"))
	depends_on("r-proc@1.16.2:", type=("build", "run"))
	depends_on("r-rms@6.1.0:", type=("build", "run"))
	depends_on("r-mice@3.12:", type=("build", "run"))
	depends_on("r-mitml@0.3.7:", type=("build", "run"))
	depends_on("r-mitools@2.4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.2:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-tidyr@1.1.2:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-car@3.0.10:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
