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

	version("4.42.0", commit="b8d9eb1b947d68f904d79c0feb1c39172852dfaa")
	version("4.36.0", commit="6cee4b80de345f36b384de47983dd6d0971a29c0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

