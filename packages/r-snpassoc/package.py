# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnpassoc(RPackage):
	"""SNPs-Based Whole Genome Association Studies

	Functions to perform most of the common analysis in genome 
    association studies are implemented. These analyses include descriptive 
    statistics and exploratory analysis of missing values, calculation of 
    Hardy-Weinberg equilibrium, analysis of association based on generalized
    linear models (either for quantitative or binary traits), and analysis
    of multiple SNPs (haplotype and epistasis analysis). Permutation test 
    and related tests (sum statistic and truncated product) are also 
    implemented. Max-statistic and genetic risk-allele score exact 
    distributions are also possible to be estimated. The methods are 
    described in Gonzalez JR et al., 2007 <doi: 10.1093/bioinformatics/btm025>.
	"""
	
	homepage = "https://github.com/isglobal-brge/SNPassoc"
	cran = "SNPassoc" 

	version("2.1-0", md5="a65247be99016d50e59b7df78ca63dfa")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-haplo-stats", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-poisbinom", type=("build", "run"))
