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

	version("1.34.0", tag="RELEASE_3_21")
	version("1.28.0", sha256="0a2cb5e298934c3542725d9b6bb65198090aa7f1a9982a5af84205c881566122")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
