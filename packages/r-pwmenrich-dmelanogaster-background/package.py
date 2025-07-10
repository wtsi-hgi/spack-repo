# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrichDmelanogasterBackground(RPackage):
	"""D. melanogaster background for PWMEnrich

	PWMEnrich pre-compiled background objects for Drosophila melanogaster and MotifDb D. melanogaster motifs.
	"""
	
	bioc = "PWMEnrich.Dmelanogaster.background" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PWMEnrich.Dmelanogaster.background_4.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PWMEnrich.Dmelanogaster.background/PWMEnrich.Dmelanogaster.background_4.36.0.tar.gz"]

	version("4.36.0", sha256="2f9e6be913ecc4d5f5c6f7d30139710f1ba232d342aa57e2c3280bb3b0f05109")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

