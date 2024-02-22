# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHacksig(RPackage):
	"""A Tidy Framework to Hack Gene Expression Signatures

	A collection of cancer transcriptomics gene signatures as well as a 
    simple and tidy interface to compute single sample enrichment scores either 
    with the original procedure or with three alternatives:
    the "combined z-score" of Lee et al. (2008) <doi:10.1371/journal.pcbi.1000217>,
    the "single sample GSEA" of Barbie et al. (2009) <doi:10.1038/nature08460> and 
    the "singscore" of Foroutan et al. (2018) <doi:10.1186/s12859-018-2435-4>.
    The 'get_sig_info()' function can be used to retrieve information about each 
    signature implemented.
	"""
	
	homepage = "https://github.com/Acare/hacksig"
	cran = "hacksig" 

	version("0.1.2", md5="6e8fe978536286d396694d5279019dab")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-future-apply@1.8.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tibble@3.1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
