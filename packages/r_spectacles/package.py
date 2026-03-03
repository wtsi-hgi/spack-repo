# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectacles(RPackage):
	"""Storing, Manipulating and Analysis Spectroscopy and Associated
Data

	Stores and eases the manipulation of spectra and associated data,
    with dedicated classes for spatial and soil-related data.
	"""
	
	homepage = "https://github.com/pierreroudier/spectacles/"
	cran = "spectacles" 

	version("0.5-4", md5="d614df71037a47298943eb850f50b7f9")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-baseline", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-epir", type=("build", "run"))
