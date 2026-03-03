# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR2mlm(RPackage):
	"""R-Squared Measures for Multilevel Models

	Generates both total- and level-specific R-squared measures from
    Rights and Sterba’s (2019) <doi:10.1037/met0000184> framework of R-squared measures for multilevel
    models with random intercepts and/or slopes, which is based on a complete
    decomposition of variance. Additionally generates graphical 
    representations of these R-squared measures to allow visualizing and 
    interpreting all measures in the framework together as an integrated set.
    This framework subsumes 10 previously-developed R-squared measures for 
    multilevel models as special cases of 5 measures from the framework, and it
    also includes several newly-developed measures. Measures in the framework 
    can be used to compute R-squared differences when comparing multilevel 
    models (following procedures in Rights & Sterba (2020) <doi:10.1080/00273171.2019.1660605>).
    Bootstrapped confidence intervals can also be calculated. To use the 
    confidence interval functionality, download bootmlm from <https://github.com/marklhc/bootmlm>.
	"""
	
	homepage = "https://github.com/mkshaw/r2mlm"
	cran = "r2mlm" 

	version("0.3.7", md5="31568ac21b6164ac49ca230ba96ddcd0")

	depends_on("r-lme4@1.1.23:", type=("build", "run"))
	depends_on("r-nlme@3.1.14:", type=("build", "run"))
	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.5:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-rlang@0.4.6:", type=("build", "run"))
	depends_on("r-rockchalk@1.8.157:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
