# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphapart(RPackage):
	"""Partition/Decomposition of Breeding Values by Paths of
Information

	A software that implements a method for partitioning genetic trends to
    quantify the sources of genetic gain in breeding programmes.
    The partitioning method is described in Garcia-Cortes et al.
    (2008) <doi:10.1017/S175173110800205X>. The package includes the
    main function AlphaPart for partitioning breeding values and auxiliary
    functions for manipulating data and summarizing, visualizing, and saving
    results.
	"""
	
	cran = "AlphaPart" 

	version("0.9.8", md5="a762b8f823431d55348a0ee0a6ca694b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-directlabels@1.1:", type=("build", "run"))
	depends_on("r-ggplot2@0.8.9:", type=("build", "run"))
	depends_on("r-pedigree@1.3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble@3.1.7:", type=("build", "run"))
