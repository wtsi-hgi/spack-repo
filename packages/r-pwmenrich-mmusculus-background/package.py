# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrichMmusculusBackground(RPackage):
	"""M. musculus background for PWMEnrich

	PWMEnrich pre-compiled background objects for M.musculus (mouse) and MotifDb M. musculus motifs.
	"""
	
	bioc = "PWMEnrich.Mmusculus.background" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PWMEnrich.Mmusculus.background_4.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PWMEnrich.Mmusculus.background/PWMEnrich.Mmusculus.background_4.36.0.tar.gz"]

	version("4.36.0", sha256="bc617782ba277a50590acab3840a6e958a5131d6c2b9dc4db98fea193d8d95bf")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

