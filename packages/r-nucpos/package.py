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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/nuCpos_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/nuCpos/nuCpos_1.20.0.tar.gz"]

	version("1.20.0", md5="b029b2678c784645c2198f00093bd923")

	depends_on("r@4.2:", type=("build", "run"))
