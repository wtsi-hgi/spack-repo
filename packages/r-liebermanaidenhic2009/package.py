# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLiebermanaidenhic2009(RPackage):
	"""Selected data from the HiC paper of E. Lieberman-Aiden et al. in Science (2009)

	This package provides data that were presented in the article "Comprehensive mapping of long-range interactions reveals folding principles of the human genome", Science 2009 Oct 9;326(5950):289-93. PMID: 19815776
	"""
	
	bioc = "LiebermanAidenHiC2009" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/LiebermanAidenHiC2009_0.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/LiebermanAidenHiC2009/LiebermanAidenHiC2009_0.40.0.tar.gz"]

	version("0.40.0", sha256="69f799ef55ae40fd2f06ecbfe1c53980802297ecbfb9b9c50de5cbaee476111b", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/LiebermanAidenHiC2009_0.40.0.tar.gz")

	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))

