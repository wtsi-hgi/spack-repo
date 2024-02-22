# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsawr(RPackage):
	"""'Pushshift' API Wrapper for 'Reddit' Submission and Comment
Search

	Connects to the API of <https://pushshift.io/> to search for 'Reddit' comments and submissions.
	"""
	
	homepage = "https://github.com/schochastics/PSAWR/"
	cran = "PSAWR" 

	version("0.1.0", md5="6809014e7ffea63096f45f02d27b9291")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
