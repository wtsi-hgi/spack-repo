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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerUNT_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerUNT/breastCancerUNT_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="2a3753cb025a2afaf8da38ebbffa76f340c5b6019641b9f063fecb0b2885215c")

	depends_on("r@2.5:", type=("build", "run"))

