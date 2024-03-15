# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGaschyhs(RPackage):
	"""ExpressionSet for response of yeast to heat shock and other environmental stresses

	Data from PMID 11102521
	"""
	
	homepage = "http://genome-www.stanford.edu/yeast_stress/data/rawdata/complete_dataset.txt"
	bioc = "gaschYHS" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/gaschYHS_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/gaschYHS/gaschYHS_1.40.0.tar.gz"]

	version("1.40.0", md5="29983eadb2a2a20f7c5475206367d641")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment