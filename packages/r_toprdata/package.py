# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToprdata(RPackage):
	"""Gene and Exon Data from Ensembl

	Gene and exon information from Ensembl genome builds GRCh38.p13 (104) and GRCh37 (v40) to use with the 'topr' package.
	"""
	
	cran = "toprdata" 

	version("1.0.2", md5="d1481f8426e1d3ca5fb98c897c7445fe")

	depends_on("r@3.5:", type=("build", "run"))
