# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProper(RPackage):
	"""PROspective Power Evaluation for RNAseq

	This package provide simulation based methods for evaluating the statistical power in differential expression analysis from RNA-seq data.
	"""
	
	bioc = "PROPER"

	version("1.40.0", commit="a99e0a6477e9693bc16bd0ca07d41938e9dc89fc")
	version("1.34.0", commit="c294c33f35ac8d4125ec4dc365bec61791a967be")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
