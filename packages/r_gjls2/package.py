# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGjls2(RPackage):
	"""A Generalized Joint Location and Scale Framework for Association
Testing

	An update to the Joint Location-Scale (JLS) testing framework that identifies associated SNPs, gene-sets and pathways with main and/or interaction effects on quantitative traits (Soave et al., 2015; <doi:10.1016/j.ajhg.2015.05.015>). The JLS method simultaneously tests the null hypothesis of equal mean and equal variance across genotypes, by aggregating association evidence from the individual location/mean-only and scale/variance-only tests using Fisher's method. The generalized joint location-scale (gJLS) framework has been developed to deal specifically with sample correlation and group uncertainty (Soave and Sun, 2017; <doi:10.1111/biom.12651>). The current release: gJLS2, include additional functionalities that enable analyses of X-chromosome genotype data through novel methods for location (Chen et al., 2021; <doi:10.1002/gepi.22422>) and scale (Deng et al., 2019; <doi:10.1002/gepi.22247>).
	"""
	
	cran = "gJLS2" 

	version("0.2.0", md5="4d76c1ce9cae269d88865d0a9387854e", url="https://cran.r-project.org/src/contrib/gJLS2_0.2.0.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
