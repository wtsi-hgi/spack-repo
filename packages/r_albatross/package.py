# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlbatross(RPackage):
	"""PARAFAC Analysis of Fluorescence Excitation-Emission Matrices

	Perform parallel factor analysis (PARAFAC: Hitchcock, 1927)
	<doi:10.1002/sapm192761164> on fluorescence excitation-emission
	matrices: handle scattering signal and inner filter effect, scale
	the dataset, fit the model; perform split-half validation or
	jack-knifing. Modified approaches such as Whittaker interpolation,
	randomised split-half, and fluorescence and scattering model
	estimation are also available. The package has a low dependency
	footprint and has been tested on a wide range of R versions.
	"""
	
	cran = "albatross" 

	version("0.3-7", md5="1d23a0682164600b2f0e055d68d1e255")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-multiway@1.0.4:", type=("build", "run"))
	depends_on("r-cmls", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
