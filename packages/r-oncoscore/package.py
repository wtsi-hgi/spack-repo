# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncoscore(RPackage):
	"""A tool to identify potentially oncogenic genes

	OncoScore is a tool to measure the association of genes to cancer based on citation frequencies in biomedical literature. The score is evaluated from PubMed literature by dynamically updatable web queries.
	"""
	
	homepage = "https://github.com/danro9685/OncoScore"
	bioc = "OncoScore" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OncoScore_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OncoScore/OncoScore_1.30.0.tar.gz"]

	version("1.30.0", sha256="335b957999e1a565b0a7ba5d13a1db7247a0d28e0caf3cf883385c3d4d42ddec")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
