# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtms(RPackage):
	"""R Toolkit for Mass Spectrometry

	Quickly imports, processes, analyzes, and visualizes mass-spectrometric 
	data.  Includes functions for easily extracting specific data and measurements
	from large (multi-gigabyte) raw Bruker data files, as well as a set of S3 object
	classes for manipulating and measuring mass spectrometric peaks and plotting
	peaks and spectra using the 'ggplot2' package.
	"""
	
	cran = "rtms" 

	version("0.2.0", md5="ae8e445d178a7686a809bca4b5fffe3e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
