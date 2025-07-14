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

	version("4.42.0", commit="e4310d9cd31b9b5ed4e55f1a3bd741dae8f7140b")
	version("4.36.0", commit="793d412ff52d7c087a44e2d8d366ed81e5a82568")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-pwmenrich", type=("build", "run"))

