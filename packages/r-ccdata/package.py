# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcdata(RPackage):
	"""Data for Combination Connectivity Mapping (ccmap) Package

	This package contains microarray gene expression data generated from the Connectivity Map build 02 and LINCS l1000. The data are used by the ccmap package to find drugs and drug combinations to mimic or reverse a gene expression signature.
	"""
	
	bioc = "ccdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/ccdata_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/ccdata/ccdata_1.28.0.tar.gz"]

	version("1.28.0", md5="60cbd595e53467fd61e1edc4f8ea47e7")

	depends_on("r@3.3:", type=("build", "run"))

	# experiment