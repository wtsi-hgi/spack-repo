# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpcrhelper(RPackage):
	"""qPCR Ct Values to Expression Values

	Computes normalized cycle threshold (Ct) values (delta Ct) from raw quantitative polymerase 
    chain reaction (qPCR) Ct values and conducts test of significance using t.test(). Plots expression 
    values based from log2(2^(-1*delta delta Ct)) across groups per gene of interest. Methods for calculation
    of delta delta Ct and relative expression (2^(-1*delta delta Ct)) values are described in: 
    Livak & Schmittgen, (2001) <doi:10.1006/meth.2001.1262>.
	"""
	
	cran = "qPCRhelper" 

	version("0.1.0", md5="ad60a0f5960d8209c8173dbf67976e56")

	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-rstatix@0.7.2:", type=("build", "run"))
	depends_on("r-ggpubr@0.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-magrittr@2.0.3:", type=("build", "run"))
