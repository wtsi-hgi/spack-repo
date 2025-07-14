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

	version("1.46.0", commit="204b76c2335c7dad92a60b328d6eddb4a3cdf8ef")
	version("1.40.0", commit="08b364f4facac29b103fd5b0331c54cfea0c5fb6")

	depends_on("r-ebimage", type=("build", "run"))

