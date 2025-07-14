# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdisop(RPackage):
	"""Decomposition of Isotopic Patterns

	Identification of metabolites using high precision mass spectrometry. MS Peaks are used to derive a ranked list of sum formulae, alternatively for a given sum formula the theoretical isotope distribution can be calculated to search in MS peak lists.
	"""
	
	homepage = "https://github.com/sneumann/Rdisop"
	bioc = "Rdisop"

	version("1.68.0", commit="c9082bf8c8a8f7588344c77d6dd9e8a74febd713")
	version("1.62.0", commit="ad6fa139d9215fdcebf7acac07a154490a0fcefa")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
