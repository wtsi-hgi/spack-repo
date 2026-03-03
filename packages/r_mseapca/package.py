# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMseapca(RPackage):
	"""Metabolite Set Enrichment Analysis for Loadings

	Computing metabolite set enrichment analysis (MSEA) (Yamamoto, H. et al. (2014) <doi:10.1186/1471-2105-15-51>) and single sample enrichment analysis (SSEA) (Yamamoto, H. (2023) <doi:10.51094/jxiv.262>).
	"""
	
	cran = "mseapca" 

	version("2.0.3", md5="7c1038cddf1e84284ddde901d145fd90")

	depends_on("r-loadings", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
