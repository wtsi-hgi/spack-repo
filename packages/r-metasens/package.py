# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetasens(RPackage):
	"""Statistical Methods for Sensitivity Analysis in Meta-Analysis

	The following methods are implemented to evaluate how sensitive the results of a meta-analysis are to potential bias in meta-analysis and to support Schwarzer et al. (2015) <DOI:10.1007/978-3-319-21416-0>, Chapter 5 'Small-Study Effects in Meta-Analysis':
 - Copas selection model described in Copas & Shi (2001) <DOI:10.1177/096228020101000402>;
 - limit meta-analysis by Rücker et al. (2011) <DOI:10.1093/biostatistics/kxq046>;
 - upper bound for outcome reporting bias by Copas & Jackson (2004) <DOI:10.1111/j.0006-341X.2004.00161.x>;
 - imputation methods for missing binary data by Gamble & Hollis (2005) <DOI:10.1016/j.jclinepi.2004.09.013> and Higgins et al. (2008) <DOI:10.1177/1740774508091600>;
 - LFK index test and Doi plot by Furuya-Kanamori et al. (2018) <DOI:10.1097/XEB.0000000000000141>.
	"""
	
	homepage = "https://github.com/guido-s/metasens"
	cran = "metasens" 

	version("1.5-2", md5="1c4b97fbf925063f2f65fccaa536c865")

	depends_on("r-meta@5.5.0:", type=("build", "run"))
