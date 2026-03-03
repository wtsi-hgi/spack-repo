# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenecycle(RPackage):
	"""Identification of Periodically Expressed Genes

	The GeneCycle package implements the approaches of Wichert
        et al. (2004) <doi:10.1093/bioinformatics/btg364>, Ahdesmaki 
        et al. (2005) <doi:10.1186/1471-2105-6-117> and Ahdesmaki et al.
        (2007) <DOI:10.1186/1471-2105-8-233> for detecting periodically 
        expressed genes from gene expression time series data.
	"""
	
	cran = "GeneCycle" 

	version("1.1.5", md5="66ead35d68cc95e6fab0d90ca45b1ca4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-longitudinal@1.1.3:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.5:", type=("build", "run"))
