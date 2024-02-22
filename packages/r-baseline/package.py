# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaseline(RPackage):
	"""Baseline Correction of Spectra

	Collection of baseline correction algorithms, along with a framework and a Tcl/Tk enabled GUI for optimising baseline algorithm parameters. Typical use of the package is for removing background effects from spectra originating from various types of spectroscopy and spectrometry, possibly optimizing this with regard to regression or classification results. Correction methods include polynomial fitting, weighted local smoothers and many more.
	"""
	
	homepage = "https://github.com/khliland/baseline/"
	cran = "baseline" 

	version("1.3-5", md5="cbb8825cc56ab6cf4ce4636cb31d2bd9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sparsem", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
