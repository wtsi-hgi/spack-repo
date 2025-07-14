# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsicsdata(RPackage):
	"""Example of 1D NMR spectra data for ASICS package

	1D NMR example spectra and additional data for use with the ASICS package. Raw 1D Bruker spectral data files were found in the MetaboLights database (https://www.ebi.ac.uk/metabolights/, study MTBLS1).
	"""
	
	bioc = "ASICSdata"

	version("1.28.0", commit="71150d9c8b87ee6672f9fa97b44d2733f3e57d50")
	version("1.22.0", commit="4ba8a30d96797324574b16fae994fe2582f7ae53")

	depends_on("r@3.5:", type=("build", "run"))

