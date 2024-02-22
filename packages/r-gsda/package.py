# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsda(RPackage):
	"""Gene Set Distance Analysis (GSDA)

	The gene-set distance analysis of omic data is implemented by generalizing distance correlations to evaluate the association of a gene set with categorical and censored event-time variables.
	"""
	
	cran = "GSDA" 

	version("1.0", md5="2d1b038d35c5fbb8049832f9b2b852f7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msigdbr", type=("build", "run"))
