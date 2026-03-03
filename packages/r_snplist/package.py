# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnplist(RPackage):
	"""Tools to Create Gene Sets

	A set of functions to create SQL tables of gene and SNP information and compose them into a SNP Set, for example to export to a PLINK set.
	"""
	
	cran = "snplist" 

	version("0.18.2", md5="8d6be4d42fb3f3c71e1cd566feae8fd9")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rsqlite@1.1:", type=("build", "run"))
	depends_on("r-biomart@2.16:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r-utils@1.27.1:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
