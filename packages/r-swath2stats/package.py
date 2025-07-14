# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwath2stats(RPackage):
	"""Transform and Filter SWATH Data for Statistical Packages

	This package is intended to transform SWATH data from the OpenSWATH software into a format readable by other statistics packages while performing filtering, annotation and FDR estimation.
	"""
	
	homepage = "https://peterblattmann.github.io/SWATH2stats/"
	bioc = "SWATH2stats"

	version("1.38.0", commit="cbc6667c8ee655069af5abe9cb36f72483f46755")
	version("1.32.1", commit="d67c0ff4b7ae3dd7804042c90418685b34443f12")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
