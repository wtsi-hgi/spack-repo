# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectralmap(RPackage):
	"""Diffusion Map and Spectral Map

	Implements the diffusion map method of dimensionality reduction and spectral method of combining multiple diffusion maps, including creation of the spectra and visualization of maps.
	"""
	
	cran = "SpectralMap" 

	version("1.0", md5="1937bb021f8fbc705bc0fdbbdc0deff9")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
