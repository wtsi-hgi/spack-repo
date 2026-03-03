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

	version("1.30.0", md5="5b61a8738f91d4c8ff214b38878a8564")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
