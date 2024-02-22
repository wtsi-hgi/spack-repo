# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrmps(RPackage):
	"""Analysis of Short Tandem Repeat (STR) Massively Parallel
Sequencing (MPS) Data

	Loading, identifying, aggregating, manipulating, and analysing short tandem repeat regions of massively parallel sequencing data in forensic genetics. 'STRMPS' can work with the package 'STRaitRazoR' (an R interface to the 'STRaitRazor' commandline tool) for added speed. 'STRaitRazoR' only works on linux and can found at <https://github.com/svilsen/STRaitRazoR>. The analyses and framework implemented in this package relies on the papers of Vilsen et al. (2017) <doi:10.1016/j.fsigen.2017.01.017> and Vilsen et al. (2018) <doi:10.1016/j.fsigen.2018.04.003>. Lastly, note that the parallelisation in the package relies on mclapply() and, thus, speed-ups will only be seen on UNIX based systems.
	"""
	
	cran = "STRMPS" 

	version("0.5.8", md5="158ea2fb641bbc439b4f0c2527f0a7a5")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
