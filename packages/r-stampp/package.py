# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStampp(RPackage):
	"""Statistical Analysis of Mixed Ploidy Populations

	Allows users to calculate pairwise Nei's Genetic Distances (Nei 1972), pairwise Fixation
 Indexes (Fst) (Weir & Cockerham 1984) and also Genomic Relationship matrixes following Yang et al. (2010) in mixed and single
 ploidy populations. Bootstrapping across loci is implemented during Fst calculation to generate confidence intervals and p-values
 around pairwise Fst values. StAMPP utilises SNP genotype data of any ploidy level (with the ability to handle missing data) and is coded to  
 utilise multithreading where available to allow efficient analysis of large datasets. StAMPP is able to handle genotype data from genlight objects 
 allowing integration with other packages such adegenet.
 Please refer to LW Pembleton, NOI Cogan & JW Forster, 2013, Molecular Ecology Resources, 13(5), 946-952. <doi:10.1111/1755-0998.12129> for the appropriate citation and user manual. Thank you in advance.
	"""
	
	homepage = "https://github.com/lpembleton/StAMPP"
	cran = "StAMPP" 

	version("1.6.3", md5="55572ba048c52d49532485790d4644a3")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-pegas", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-adegenet", type=("build", "run"))
