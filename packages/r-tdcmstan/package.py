# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdcmstan(RPackage):
	"""Automating the Creation of Stan Code for TDCMs

	A collection of functions for automatically creating 'Stan'
      code for transition diagnostic classification models (TDCMs) as they are
      defined by Madison and Bradshaw (2018) <DOI:10.1007/s11336-018-9638-5>.
      This package supports automating the creation of 'Stan' code for TDCMs,
      fungible TDCMs (i.e., TDCMs with item parameters constrained to be equal
      across all items), and multi-threaded TDCMs.
	"""
	
	homepage = "https://github.com/atlas-aai/tdcmStan"
	cran = "tdcmStan" 

	version("3.0.0", md5="bcc21af817ca2fa341a64bbba263645b")
	version("2.0.0", md5="9f3dfdefb63240140aa783393c8fb640")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1.0.7:", type=("build", "run"))
	depends_on("r-glue@1.4.2:", type=("build", "run"))
	depends_on("r-magrittr@2.0.1:", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-tibble@3.1.5:", type=("build", "run"))
	depends_on("r-tidyr@1.1.4:", type=("build", "run"))
	depends_on("r-tidyselect@1.1.2:", type=("build", "run"))
