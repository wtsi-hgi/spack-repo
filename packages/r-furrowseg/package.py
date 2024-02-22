# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFurrowseg(RPackage):
	"""Furrow Segmentation

	Image feature data and analysis codes for the Guglielmi, Barry et al. paper describing the application of an optogenetics tools to disrupt Drosophila embryo furrowing.
	"""
	
	bioc = "furrowSeg" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/furrowSeg_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/furrowSeg/furrowSeg_1.30.0.tar.gz"]

	version("1.30.0", md5="f41e88a4d47949b3b8b126b0fc7852eb")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))

	# experiment