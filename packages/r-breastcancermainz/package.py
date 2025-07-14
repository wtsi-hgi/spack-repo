# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBreastcancermainz(RPackage):
	"""Gene expression dataset published by Schmidt et al. [2008] (MAINZ).

	Gene expression data from the breast cancer study published by Schmidt et al. in 2008, provided as an eSet.
	"""
	
	homepage = "http://compbio.dfci.harvard.edu/"
	bioc = "breastCancerMAINZ" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerMAINZ_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerMAINZ/breastCancerMAINZ_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="94d4df826ac90df470e21ef8fe947ae21012c1e78a460511ba404d0216537bd9")

	depends_on("r@2.5:", type=("build", "run"))

