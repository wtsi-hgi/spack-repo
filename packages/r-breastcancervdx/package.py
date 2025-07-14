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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerVDX_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerVDX/breastCancerVDX_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="c03d04aa3e347b6153f0f68cc38218a4f8a93957386ce43b03596b3028fe288b")

	depends_on("r@2.5:", type=("build", "run"))

