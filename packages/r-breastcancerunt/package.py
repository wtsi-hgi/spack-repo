# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancerunt(RPackage):
	"""Gene expression dataset published by Sotiriou et al. [2007] (UNT).

	Gene expression data from a breast cancer study published by Sotiriou et al. in 2007, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerUNT" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/breastCancerUNT_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/breastCancerUNT/breastCancerUNT_1.40.0.tar.gz"]

	version("1.40.0", md5="31e1b6d7e34b4acb9207e3e152539166")

	depends_on("r@2.5:", type=("build", "run"))

	# experiment