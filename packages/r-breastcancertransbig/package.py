# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancertransbig(RPackage):
	"""Gene expression dataset published by Desmedt et al. [2007] (TRANSBIG).

	Gene expression data from a breast cancer study published by Desmedt et al. in 2007, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerTRANSBIG" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/breastCancerTRANSBIG_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/breastCancerTRANSBIG/breastCancerTRANSBIG_1.40.0.tar.gz"]

	version("1.40.0", md5="170d89ddd3e554da50a0b2b5d040a96e")

	depends_on("r@2.5:", type=("build", "run"))

	# experiment