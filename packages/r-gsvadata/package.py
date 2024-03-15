# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsvadata(RPackage):
	"""Data employed in the vignette of the GSVA package

	This package stores the data employed in the vignette of the GSVA package. These data belong to the following publications: Armstrong et al. Nat Genet 30:41-47, 2002; Cahoy et al. J Neurosci 28:264-278, 2008; Carrel and Willard, Nature, 434:400-404, 2005; Huang et al. PNAS, 104:9758-9763, 2007; Pickrell et al. Nature, 464:768-722, 2010; Skaletsky et al. Nature, 423:825-837; Verhaak et al. Cancer Cell 17:98-110, 2010
	"""
	
	bioc = "GSVAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/GSVAdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/GSVAdata/GSVAdata_1.38.0.tar.gz"]

	version("1.38.0", md5="3c2d6a66967ab8c3c2545fc3323282b3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-hgu95a-db", type=("build", "run"))

	# experiment