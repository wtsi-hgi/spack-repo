# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipseqdbdata(RPackage):
	"""Data for the chipseqDB Workflow

	Sorted and indexed BAM files for ChIP-seq libraries, for use in the chipseqDB workflow. BAM indices are also included.
	"""
	
	bioc = "chipseqDBData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/chipseqDBData_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/chipseqDBData/chipseqDBData_1.18.0.tar.gz"]

	version("1.18.0", md5="a6e50016d2d7c0cb085df2c4254b5f84")

	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

	# experiment