# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPepsnmr(RPackage):
	"""Pre-process 1H-NMR FID signals

	This package provides R functions for common pre-procssing steps that are applied on 1H-NMR data. It also provides a function to read the FID signals directly in the Bruker format.
	"""
	
	homepage = "https://github.com/ManonMartin/PepsNMR"
	bioc = "PepsNMR"

	version("1.26.0", commit="5216333c5444a1ef6b18cecd8e234f4f4b3fff68")
	version("1.20.0", commit="35ef5cdf34f0b6ce599a15c1e40f8bfa6b1683ec")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ptw", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
