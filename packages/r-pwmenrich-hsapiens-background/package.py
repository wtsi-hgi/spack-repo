# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwmenrichHsapiensBackground(RPackage):
	"""H. sapiens background for PWMEnrich

	PWMEnrich pre-compiled background objects for H. sapiens (human) and MotifDb H. sapiens motifs.
	"""
	
	bioc = "PWMEnrich.Hsapiens.background" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/PWMEnrich.Hsapiens.background_4.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/PWMEnrich.Hsapiens.background/PWMEnrich.Hsapiens.background_4.36.0.tar.gz"]

	version("4.36.0", md5="7c7b177c29fc31c7546d4e7160a9b977")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

	# experiment