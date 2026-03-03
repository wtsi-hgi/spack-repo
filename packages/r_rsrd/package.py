# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsrd(RPackage):
	"""Sum of Ranking Differences Statistical Test

	We provide an implementation for Sum of Ranking Differences (SRD), 
    a novel statistical test introduced by Héberger (2010) 
    <doi:10.1016/j.trac.2009.09.009>. The test allows the comparison of 
    different solutions through a reference by first performing a rank 
    transformation on the input, then calculating and comparing the distances 
    between the solutions and the reference - the latter is measured in the 
    L1 norm. The reference can be an external benchmark (e.g. an established 
    gold standard) or can be aggregated from the data. The calculated distances, 
    called SRD scores, are validated in two ways, see Héberger and Kollár-Hunek 
    (2011) <doi:10.1002/cem.1320>. A randomization test (also called permutation 
    test) compares the SRD scores of the solutions to the SRD scores of randomly 
    generated rankings. The second validation option is cross-validation that 
    checks whether the rankings generated from the solutions come from the same 
    distribution or not. For a detailed analysis about the cross-validation 
    process see Sziklai, Baranyi and Héberger (2021) <arXiv:2105.11939>. The 
    package offers a wide array of features related to SRD including the computation 
    of the SRD scores, validation options, input preprocessing and plotting tools. 
	"""
	
	cran = "rSRD" 

	version("0.1.7", md5="b66f8f271467f43a30df558b2e16fb2c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
