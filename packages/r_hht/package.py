# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHht(RPackage):
	"""The Hilbert-Huang Transform: Tools and Methods

	Builds on the EMD package to provide additional tools for empirical mode decomposition (EMD) and Hilbert spectral analysis. It also implements the ensemble empirical decomposition (EEMD) and the complete ensemble empirical mode decomposition (CEEMD) methods to avoid mode mixing and intermittency problems found in EMD analysis.  The package comes with several plotting methods that can be used to view intrinsic mode functions, the HHT spectrum, and the Fourier spectrum. 
	"""
	
	cran = "hht" 

	version("2.1.6", md5="0f3c5dce5a1578356f99aab0e37ce6f1")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-emd@1.5.5:", type=("build", "run"))
	depends_on("r-fields@6.7.6:", type=("build", "run"))
