# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTigerr(RPackage):
	"""Technical Variation Elimination with Ensemble Learning
Architecture

	
    The R implementation of TIGER. 
    TIGER integrates random forest algorithm into an innovative ensemble learning architecture. Benefiting from this advanced architecture, TIGER is resilient to outliers, free from model tuning and less likely to be affected by specific hyperparameters.
    TIGER supports targeted and untargeted metabolomics data and is competent to perform both intra- and inter-batch technical variation removal. TIGER can also be used for cross-kit adjustment to ensure data obtained from different analytical assays can be effectively combined and compared.
    Reference: Han S. et al. (2022) <doi:10.1093/bib/bbab535>.
	"""
	
	cran = "TIGERr" 

	version("1.0.0", md5="7bec261df646f7b211a50b295347ad75")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-pbapply@1.4.3:", type=("build", "run"))
	depends_on("r-ppcor@1.1:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
