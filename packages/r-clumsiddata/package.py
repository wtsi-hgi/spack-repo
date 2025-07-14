# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClumsiddata(RPackage):
	"""Data for the CluMSID package

	This package contains various LC-MS/MS and GC-MS data that is used in vignettes and examples in the CluMSID package.
	"""
	
	bioc = "CluMSIDdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CluMSIDdata_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CluMSIDdata/CluMSIDdata_1.18.0.tar.gz"]

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="1aaa23ff5b521f175a91eaeb3c605ec3e81823853b2062deeb87a18528f05075")

	depends_on("r@3.6:", type=("build", "run"))

