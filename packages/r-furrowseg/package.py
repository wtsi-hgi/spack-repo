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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/furrowSeg_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/furrowSeg/furrowSeg_1.30.0.tar.gz"]

	version("1.30.0", sha256="72d8918525b80efbe3fecbf913993962e2c70a28426df6182ef0700f4a4f796f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))

