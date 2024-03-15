# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbamethyl(RPackage):
	"""Model-based analysis of DNA methylation data

	This package provides a function for reconstructing DNA methylation values from raw measurements. It iteratively implements the group fused lars to smooth related-by-location methylation values and the constrained least squares to remove probe affinity effect across multiple sequences.
	"""
	
	bioc = "MBAmethyl" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MBAmethyl_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MBAmethyl/MBAmethyl_1.36.0.tar.gz"]

	version("1.36.0", md5="0b6ac0d76525c156606d08bcbf606709")

	depends_on("r@2.15:", type=("build", "run"))
