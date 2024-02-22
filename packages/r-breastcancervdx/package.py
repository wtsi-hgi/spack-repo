# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancervdx(RPackage):
	"""Gene expression datasets published by Wang et al. [2005] and Minn et al. [2007] (VDX).

	Gene expression data from a breast cancer study published by Wang et al. in 2005 and Minn et al. in 2007, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerVDX" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/breastCancerVDX_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/breastCancerVDX/breastCancerVDX_1.40.0.tar.gz"]

	version("1.40.0", md5="446ef46e0bdd1480e12de21ded7b58f0")

	depends_on("r@2.5:", type=("build", "run"))

	# experiment