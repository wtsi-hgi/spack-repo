# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFactdesign(RPackage):
	"""Factorial designed microarray experiment analysis

	This package provides a set of tools for analyzing data from a factorial designed microarray experiment, or any microarray experiment for which a linear model is appropriate. The functions can be used to evaluate tests of contrast of biological interest and perform single outlier detection.
	"""
	
	bioc = "factDesign" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/factDesign_1.78.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/factDesign/factDesign_1.78.0.tar.gz"]

	version("1.78.0", md5="774d444f3227bbac6bc13e48d3974b20")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))
