# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMgfr(RPackage):
	"""Marker Gene Finder in RNA-seq data

	The package is designed to detect marker genes from RNA-seq data.
	"""
	
	bioc = "MGFR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MGFR_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MGFR/MGFR_1.28.0.tar.gz"]

	version("1.28.0", md5="73cad34ad523499dbdcfb3746b519b48")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
