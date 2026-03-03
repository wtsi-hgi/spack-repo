# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RI18n(RPackage):
	"""Internationalization Data from the 'Unicode CLDR' in Tabular
Form

	Up-to-date data from the 'Unicode CLDR Project' (where 'CLDR'
    stands for 'Common Locale Data Repository') are available here as a series
    of easy-to-parse datasets. Several functions are provided for extracting
    key elements from the tabular datasets.
	"""
	
	homepage = "https://github.com/rich-iannone/i18n"
	cran = "i18n" 

	version("0.2.0", md5="b2e0b053cc51d8ddcdb4f7adae34d38b")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
