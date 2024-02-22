# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSiberg(RPackage):
	"""Systematic Identification of Bimodally Expressed Genes Using
RNAseq Data

	Provides models to identify bimodally expressed genes from
 RNAseq data based on the Bimodality Index. SIBERG models the  RNAseq data in
 the finite mixture modeling framework and incorporates mechanisms  for
 dealing with RNAseq normalization. Three types of mixture models are
 implemented,  namely, the mixture of log normal, negative binomial, or 
 generalized Poisson distribution. See Tong et al. (2013)
 <doi:10.1093/bioinformatics/bts713>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "SIBERG" 

	version("2.0.3", md5="688a8fd379177cab60c43fbd7c373d93")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
