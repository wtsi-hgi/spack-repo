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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/breastCancerTRANSBIG_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/breastCancerTRANSBIG/breastCancerTRANSBIG_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="4dd9e78b4032967ffc46be7dec0ccbb8d0d3f9f78533588e50e8deb858f2090f")

	depends_on("r@2.5:", type=("build", "run"))

