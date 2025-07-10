# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtdata(RPackage):
	"""Data companion to CTexploreR

	Data from publicly available databases (GTEx, CCLE, TCGA and ENCODE) that go with CTexploreR in order to re-define a comprehensive and thoroughly curated list of CT genes and their main characteristics.
	"""
	
	bioc = "CTdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/CTdata_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/CTdata/CTdata_1.2.0.tar.gz"]

	version("1.2.0", sha256="86ffadabf93b0537448d214c61db5e10ca6f24b258016685b42debb40ab2c5bd")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
