# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyperspec(RPackage):
	"""Work with Hyperspectral Data, i.e. Spectra + Meta Information
(Spatial, Time, Concentration, ...)

	Comfortable ways to work with hyperspectral data sets.
    I.e. spatially or time-resolved spectra, or spectra with any other kind
    of information associated with each of the spectra. The spectra can be data
    as obtained in XRF, UV/VIS, Fluorescence, AES, NIR, IR, Raman, NMR, MS,
    etc. More generally, any data that is recorded over a discretized variable,
    e.g. absorbance = f(wavelength), stored as a vector of absorbance values
    for discrete wavelengths is suitable.
	"""
	
	homepage = "https://r-hyperspec.github.io/hyperSpec/"
	cran = "hyperSpec" 

	version("0.100.0", md5="d665f9211c705b23899d4e0691a3c759")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
