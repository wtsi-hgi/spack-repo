# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPheindicatormethods(RPackage):
	"""Common Public Health Statistics and their Confidence Intervals

	Functions to calculate commonly used public health statistics and 
    their confidence intervals using methods approved for use in the production  
    of Public Health England indicators such as those presented via Fingertips 
    (<http://fingertips.phe.org.uk/>). It provides functions for the generation 
    of proportions, crude rates, means, directly standardised rates, indirectly 
    standardised rates, standardised mortality ratios, slope and relative index
    of inequality and life expectancy. 
    Statistical methods are referenced in the following publications. 
    Breslow NE, Day NE (1987) <doi:10.1002/sim.4780080614>.
    Dobson et al (1991) <doi:10.1002/sim.4780100317>. 
    Armitage P, Berry G (2002) <doi:10.1002/9780470773666>.
    Wilson EB. (1927) <doi:10.1080/01621459.1927.10502953>.
    Altman DG et al (2000, ISBN: 978-0-727-91375-3).
    Chiang CL. (1968, ISBN: 978-0-882-75200-6).
    Newell C. (1994, ISBN: 978-0-898-62451-9).
    Eayres DP, Williams ES (2004) <doi:10.1136/jech.2003.009654>.
    Silcocks PBS et al (2001) <doi:10.1136/jech.55.1.38>.
    Low and Low (2004) <doi:10.1093/pubmed/fdh175>.
	"""
	
	cran = "PHEindicatormethods" 

	version("2.0.2", md5="430838a915c6f87311ec08de785bdada")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect@1.2:", type=("build", "run"))
	depends_on("r-tidyr@1.3:", type=("build", "run"))
