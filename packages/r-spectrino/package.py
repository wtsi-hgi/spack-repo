# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectrino(RPackage):
	"""Spectra Viewer, Organizer, Data Preparation and Property Blocks

	Spectra viewer, organizer, data preparation and property blocks
        from within R or stand-alone. Binary (application) part is 
        installed separately using spnInstallApp() from spectrino package.
	"""
	
	homepage = "http://www.spectrino.com"
	cran = "spectrino" 

	version("2.0.0", md5="0caffb5def2467ab5d4ff504115ff079")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
