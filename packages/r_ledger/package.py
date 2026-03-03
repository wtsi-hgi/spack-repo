# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLedger(RPackage):
	"""Utilities for Importing Data from Plain Text Accounting Files

	Utilities for querying plain text accounting files from 'Ledger', 'HLedger', and 'Beancount'.
	"""
	
	homepage = "https://github.com/trevorld/r-ledger"
	cran = "ledger" 

	version("2.0.9", md5="1bc7f9936ca27d25e5147dbcee55b860")

	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@0.7:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
