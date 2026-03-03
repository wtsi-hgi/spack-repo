# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLibbib(RPackage):
	"""Various Utilities for Library Science/Assessment and Cataloging

	Provides functions for validating and normalizing bibliographic
   codes such as ISBN, ISSN, and LCCN. Also includes functions to communicate
   with the WorldCat API, translate Call numbers (Library of Congress and
   Dewey Decimal) to their subject classifications or subclassifications,
   and provides various loadable data files such call number / subject
   crosswalks and code tables.
	"""
	
	cran = "libbib" 

	version("1.6.4", md5="4e0c97d94b6ed5f7e967f1fa2f18d96c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
