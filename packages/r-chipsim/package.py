# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipsim(RPackage):
	"""Simulation of ChIP-seq experiments

	A general framework for the simulation of ChIP-seq data. Although currently focused on nucleosome positioning the package is designed to support different types of experiments.
	"""
	
	bioc = "ChIPsim"

	version("1.62.0", commit="d3799438d7200d7e738828a72c9a60f143959fb9")
	version("1.56.0", commit="c3ecaa6d3f4907d9014a07b2240824dbb958aaa7")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
