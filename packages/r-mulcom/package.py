# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulcom(RPackage):
	"""Calculates Mulcom test

	Identification of differentially expressed genes and false discovery rate (FDR) calculation by Multiple Comparison test.
	"""
	
	bioc = "Mulcom" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Mulcom_1.52.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Mulcom/Mulcom_1.52.0.tar.gz"]

	version("1.52.0", md5="87375077f62104b18567db2e68a07488")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
