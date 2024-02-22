# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfc(RPackage):
	"""Log Fold Change Distribution Tools for Working with Ratios of
Counts

	Ratios of count data such as obtained from RNA-seq are modelled
    using Bayesian statistics to derive posteriors for effects sizes. This
    approach is described in Erhard & Zimmer (2015) <doi:10.1093/nar/gkv696> 
    and Erhard (2018) <doi:10.1093/bioinformatics/bty471>.
	"""
	
	homepage = "https://github.com/erhard-lab/lfc"
	cran = "lfc" 

	version("0.2.3", md5="fcbef66d12f023b521d7a7ef0f3aea76")

