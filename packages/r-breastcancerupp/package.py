# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancerupp(RPackage):
	"""Gene expression dataset published by Miller et al. [2005] (UPP).

	Gene expression data from a breast cancer study published by Miller et al. in 2005, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerUPP" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerUPP_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerUPP/breastCancerUPP_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="d75880feff1c0a8c10ff9c24179229ae18144d074c044a58edd9bbd3176e2956")

	depends_on("r@2.5:", type=("build", "run"))

