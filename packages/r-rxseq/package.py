# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxseq(RPackage):
	"""Combined Total and Allele Specific Reads Sequencing Study

	Analysis of combined total and allele specific reads from the reciprocal cross study with RNA-seq data.  
	"""
	
	cran = "rxSeq" 

	version("0.99.3", md5="84a32b4889bbda46e3ae8780c01b6d8d")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
