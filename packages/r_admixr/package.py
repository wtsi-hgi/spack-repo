# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmixr(RPackage):
	"""An Interface for Running 'ADMIXTOOLS' Analyses

	An interface for performing all stages of 'ADMIXTOOLS' analyses
	(<https://reich.hms.harvard.edu/software>) entirely from R. Wrapper functions
	(D, f4, f3, etc.) completely automate the generation of intermediate
	configuration files, run 'ADMIXTOOLS' programs on the command-line, and
	parse output files to extract values of interest. This allows users to focus
	on the analysis itself instead of worrying about low-level technical details.
	A set of complementary functions for processing and filtering of data in
	the 'EIGENSTRAT' format is also provided.
	"""
	
	homepage = "https://github.com/bodkan/admixr"
	cran = "admixr"

	version("0.9.1", md5="4d93e5c867a34ffec51d421d40e68aa8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("admixtools", type=("build", "link", "run"))
