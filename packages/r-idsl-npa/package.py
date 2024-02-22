# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdslNpa(RPackage):
	"""Nominal Peak Analysis (NPA)

	A pipeline to process nominal mass spectrometry data to create .msp files for untargeted analyses.
	"""
	
	homepage = "https://github.com/idslme/idsl.npa"
	cran = "IDSL.NPA" 

	version("1.2", md5="a09906ff3ab9c332278d46d13d9cccf9")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-idsl-mxp", type=("build", "run"))
	depends_on("r-idsl-ipa", type=("build", "run"))
	depends_on("r-idsl-fsa", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
