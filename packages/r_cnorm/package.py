# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnorm(RPackage):
	"""Continuous Norming

	Conventional methods for producing standard scores or percentiles 
    in psychometrics or biometrics are often plagued with 'jumps' or 'gaps' 
    (i.e., discontinuities) in norm tables and low confidence for assessing 
    extreme scores. The continuous norming method introduced by A. Lenhard et al.
    (2016, <doi:10.1177/1073191116656437>; 2019, <doi:10.1371/journal.pone.0222279>;
    2021 <doi: 10.1177/0013164420928457>) estimates percentile development 
    (e. g. over age) and generates continuous test norm scores on the basis of 
    the raw data from standardization samples, without requiring assumptions 
    about the distribution of the raw data: Norm scores are directly established 
    from raw data by modeling the latter ones as a function of both percentile 
    scores and an explanatory variable (e.g., age). The method minimizes bias 
    arising from sampling and measurement error, while handling marked deviations 
    from normality, addressing bottom or ceiling effects and capturing almost 
    all of the variance in the original norm data sample. It includes procedures 
    for post stratification of norm samples to overcome bias in data collection 
    and to mitigate violations of representativeness. An online demonstration is 
    available via <https://cnorm.shinyapps.io/cNORM/>.
	"""
	
	homepage = "https://www.psychometrica.de/cNorm_en.html"
	cran = "cNORM" 

	version("3.0.4", md5="84c7d5ad32e7b0eec68ee51f1253496a")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-lattice@0.21:", type=("build", "run"))
	depends_on("r-leaps@3.1:", type=("build", "run"))
	depends_on("r-latticeextra@0.6:", type=("build", "run"))
