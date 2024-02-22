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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/CTdata_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/CTdata/CTdata_1.2.0.tar.gz"]

	version("1.2.0", md5="d130308cf078329f4cc6a1cc8055475d")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
