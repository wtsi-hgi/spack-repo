# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRseis(RPackage):
	"""Seismic Time Series Analysis Tools

	Multiple interactive codes to view and analyze seismic data, via spectrum analysis, wavelet transforms, particle motion, hodograms.  Includes general time-series tools, plotting, filtering, interactive display.
	"""
	
	cran = "RSEIS" 

	version("4.2-0", md5="1e48488c5c3420d62970461cead4195f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rpmg", type=("build", "run"))
	depends_on("r-rwave", type=("build", "run"))
