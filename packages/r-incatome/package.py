# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncatome(RPackage):
	"""Internal Control Analysis of Translatome Studies by Microarrays

	Data analysis, normalisation and differential expression for Translatome studies by microarrays (T Sbarrato et al. RNA. 2017 Aug 25; <DOI:10.1261/rna.060525.116>).
	"""
	
	cran = "INCATome" 

	version("1.0", md5="c70614749d110b159ad1670b4dbc5dfe")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-multtest", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-rankprod", type=("build", "run"))
