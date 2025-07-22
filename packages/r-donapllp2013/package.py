# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDonapllp2013(RPackage):
	"""Supplementary data package for Dona et al. (2013) containing example images and tables

	An experiment data package associated with the publication Dona et al. (2013). Package contains runnable vignettes showing an example image segmentation for one posterior lateral line primordium, and also the data table and code used to analyze tissue-scale lifetime-ratio statistics.
	"""
	
	bioc = "DonaPLLP2013" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DonaPLLP2013_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/DonaPLLP2013/DonaPLLP2013_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="006f01ffccf41dbf3ccc445c011d2481ecbf49a88bee1a8eec4ebd36b379bd5f", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/DonaPLLP2013_1.40.0.tar.gz")

	depends_on("r-ebimage", type=("build", "run"))

