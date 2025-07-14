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

    version("1.58.0", tag="RELEASE_3_21")
	version("1.52.0", sha256="450e19d117074b6e9a0690cefc6b2dda42f31a8cabf264d86d90e4a250705b97")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
