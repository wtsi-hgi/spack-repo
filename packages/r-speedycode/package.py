# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpeedycode(RPackage):
	"""Automate Code for Adding Labels, Recoding and Renaming
Variables, and Converting ASCII Files

	Label, recode, rename, and convert datasets and ASCII files more efficiently. 'speedycode' automates the code necessary for labeling variables with the 'labelled' package, recoding and renaming variables with 'dplyr' syntax, and converting ASCII files with the 'readroper' package. Most functions require only the name of the dataset and the code will be automatically written. Some convenience functions useful for converting ASCII files are also included.
	"""
	
	cran = "speedycode" 

	version("0.3.0", md5="8d7f9055d035a98dc252b462faeb752f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
