# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwr2ppl(RPackage):
	"""Power Analyses for Common Designs (Power to the People)

	Statistical power analysis for designs including t-tests, correlations, 
    multiple regression, ANOVA, mediation, and logistic regression. Functions accompany 
    Aberson (2019) <doi:10.4324/9781315171500>.
	"""
	
	cran = "pwr2ppl" 

	version("0.5.0", md5="3d6dd18174ec00f164d3d7cffa9f132e")

	depends_on("r-car@3.0.0:", type=("build", "run"))
	depends_on("r-mass@7.3.51:", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-tidyr@0.8:", type=("build", "run"))
	depends_on("r-ez@0.4.3:", type=("build", "run"))
	depends_on("r-nlme@3.1.139:", type=("build", "run"))
	depends_on("r-phia@0.2.0:", type=("build", "run"))
	depends_on("r-afex@0.22.1:", type=("build", "run"))
	depends_on("r-mbess@4.5:", type=("build", "run"))
	depends_on("r-lavaan@0.6.2:", type=("build", "run"))
	depends_on("r-semtools@0.5:", type=("build", "run"))
	depends_on("r-quantreg@5.50:", type=("build", "run"))
	depends_on("r-broom@0.7:", type=("build", "run"))
	depends_on("r-lmtest@0.9.30:", type=("build", "run"))
	depends_on("r-lmperm", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
