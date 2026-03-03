# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTidyfst(RPackage):
	"""Tidy Verbs for Fast Data Manipulation

	A toolkit of tidy data manipulation verbs with 'data.table' as the backend.
  Combining the merits of syntax elegance from 'dplyr' and computing performance from 'data.table', 
  'tidyfst' intends to provide users with state-of-the-art data manipulation tools with least pain.
  This package is an extension of 'data.table'. While enjoying a tidy syntax, 
  it also wraps combinations of efficient functions to facilitate frequently-used data operations.  
	"""
	
	homepage = "https://github.com/hope-data-science/tidyfst"
	cran = "tidyfst" 

	version("1.7.7", md5="61ea7dbb1588b18ef2fa51cb23cff791")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table@1.13:", type=("build", "run"))
	depends_on("r-fst@0.9:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
