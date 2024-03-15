# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInformeasure(RPackage):
	"""R implementation of information measurements

	This package consolidates a comprehensive set of information measurements, encompassing mutual information, conditional mutual information, interaction information, partial information decomposition, and part mutual information.
	"""
	
	homepage = "https://github.com/chupan1218/Informeasure"
	bioc = "Informeasure" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Informeasure_1.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Informeasure/Informeasure_1.12.1.tar.gz"]

	version("1.12.1", md5="cdff7352eb6dcf4a514d413761087dc1")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
