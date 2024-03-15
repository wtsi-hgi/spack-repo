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

	version("4.36.0", md5="b671ba0cff5c0c6017fd3f72d0afc547")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

	# experiment