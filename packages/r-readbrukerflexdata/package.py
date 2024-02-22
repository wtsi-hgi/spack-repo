# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadbrukerflexdata(RPackage):
	"""Reads Mass Spectrometry Data in Bruker *flex Format

	Reads data files acquired by Bruker Daltonics' matrix-assisted
    laser desorption/ionization-time-of-flight mass spectrometer of the *flex
    series.
	"""
	
	homepage = "https://strimmerlab.github.io/software/maldiquant/"
	cran = "readBrukerFlexData" 

	version("1.9.2", md5="c696d075e8971861c9d96ba5d3b2e9fd")

	depends_on("r@3.3:", type=("build", "run"))
