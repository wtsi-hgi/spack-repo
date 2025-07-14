# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucpos(RPackage):
	"""An R package for prediction of nucleosome positions

	nuCpos, a derivative of NuPoP, is an R package for prediction of nucleosome positions. nuCpos calculates local and whole nucleosomal histone binding affinity (HBA) scores for a given 147-bp sequence. Note: This package was designed to demonstrate the use of chemical maps in prediction. As the parental package NuPoP now provides chemical-map-based prediction, the function for dHMM-based prediction was removed from this package. nuCpos continues to provide functions for HBA calculation.
	"""
	
	bioc = "nuCpos"

	version("1.26.0", commit="24a97ac2b50c83e20354e8fa0c696bc997710d53")
	version("1.20.0", commit="8326dcc0e87626874c2fe17685a75bced663ed82")

	depends_on("r@4.2:", type=("build", "run"))
