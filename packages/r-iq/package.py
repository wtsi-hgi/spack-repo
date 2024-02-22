# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIq(RPackage):
	"""Protein Quantification in Mass Spectrometry-Based Proteomics

	An implementation of the MaxLFQ algorithm by
    Cox et al. (2014) <doi:10.1074/mcp.M113.031591> in a comprehensive
    pipeline for processing proteomics data in data-independent acquisition mode
    (Pham et al. 2020 <doi:10.1093/bioinformatics/btz961>).
    It offers additional options for protein quantification using
    the N most intense fragment ions, using all fragment ions, and
    a wrapper for the median polish algorithm by Tukey (1977, ISBN:0201076160).
    In general, the tool can be used to integrate multiple 
    proportional observations into a single quantitative value.
	"""
	
	homepage = "https://github.com/tvpham/iq"
	cran = "iq" 

	version("1.9.12", md5="0405be1778756fc4e3ccd2e8d71fdb15")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
