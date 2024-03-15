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

	version("1.18.0", md5="315da29d9f052e0abfbad59be9606f34")

	depends_on("r@3.6:", type=("build", "run"))

	# experiment