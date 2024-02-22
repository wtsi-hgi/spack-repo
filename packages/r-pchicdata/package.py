# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPchicdata(RPackage):
	"""Promoter Capture Hi-C data

	Subsets of Promoter Capture Hi-C data conveniently packaged for Chicago users. Data includes interactions detected for chromosomes 20 and 21 in GM12878 cells and for chromosomes 18 and 19 in mESC.
	"""
	
	bioc = "PCHiCdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/PCHiCdata_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/PCHiCdata/PCHiCdata_1.30.0.tar.gz"]

	version("1.30.0", md5="8791902075a44ae03c0366150aa3f61e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-chicago", type=("build", "run"))

	# experiment