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

	version("4.42.0", tag="RELEASE_3_21")
	version("4.36.0", sha256="5ca247a8975146e4b5bb0a56db233b128dadda30c3f92bebd51da5596039273b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

