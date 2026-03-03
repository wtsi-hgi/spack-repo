# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombatEnigma(RPackage):
	"""Fit and Apply ComBat Harmonization for ENIGMA

	Fit and apply ComBat to harmonize magnetic resonance imaging (MRI) data from different sites. Briefly, ComBat is a batch adjustment method that removes additive and multiplicative differences between sites due to the use of different scanning devices. As detailed in the manual, the original function was first modified for the harmonization of MRI data (Fortin et al. (2017) <doi:10.1016/j.neuroimage.2017.11.024>) and then modified again to create separate functions for fitting and applying the harmonization and allow missing values and constant rows for its use within the Enhancing Neuro Imaging Genetics through Meta-Analysis (ENIGMA) Consortium (Radua et al. (2020) <doi:10.1016/j.neuroimage.2017.11.024>). This package includes the latter version.
	"""
	
	cran = "combat.enigma" 

	version("1.0", md5="d6e7f7f68df7570ba8649ef0dc83aff2")

	depends_on("r@2.10:", type=("build", "run"))
