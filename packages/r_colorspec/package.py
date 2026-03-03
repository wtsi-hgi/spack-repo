# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RColorspec(RPackage):
	"""Color Calculations with Emphasis on Spectral Data

	Calculate with spectral properties of light sources, materials, cameras, eyes, and scanners.
    Build complex systems from simpler parts using a spectral product algebra. For light sources,
    compute CCT, CRI, and SSI.  For object colors, compute optimal colors and Logvinenko coordinates.
    Work with the standard CIE illuminants and color matching functions, and read spectra from 
    text files, including CGATS files.  Estimate a spectrum from its response. A user guide and 9 vignettes are included.
	"""
	
	cran = "colorSpec" 

	version("1.5-0", md5="17316e77b548bcedb8d478ded07cb930")

	depends_on("r@3.5:", type=("build", "run"))
