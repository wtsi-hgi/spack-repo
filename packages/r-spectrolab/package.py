# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectrolab(RPackage):
	"""Class and Methods for Spectral Data

	Input/Output, processing and visualization of spectra taken with different spectrometers, including SVC (Spectra Vista), ASD and PSR (Spectral Evolution). Implements an S3 class 'spectra' that other packages can build on. Provides methods to access, plot, manipulate, splice sensor overlap, vector normalize and smooth spectra.
	"""
	
	homepage = "https://CRAN.R-project.org/package=spectrolab"
	cran = "spectrolab" 

	version("0.0.18", md5="c6aa066de20e3773a4cf5b66c80c4b5b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1:", type=("build", "run"))
	depends_on("r-shiny@1.5:", type=("build", "run"))
	depends_on("r-shinyjs@1.1:", type=("build", "run"))
