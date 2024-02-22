# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringx(RPackage):
	"""Replacements for Base String Functions Powered by 'stringi'

	English is the native language for only 5% of the World population.
    Also, only 17% of us can understand this text. Moreover, the Latin alphabet
    is the main one for merely 36% of the total.
    The early computer era, now a very long time ago, was dominated by the US.
    Due to the proliferation of the internet, smartphones, social media, and
    other technologies and communication platforms, this is no longer the case.
    This package replaces base R string functions (such as grep(),
    tolower(), sprintf(), and strptime()) with ones that fully
    support the Unicode standards related to natural language and
    date-time processing. It also fixes some long-standing inconsistencies,
    and introduces some new, useful features.
    Thanks to 'ICU' (International Components for Unicode) and 'stringi',
    they are fast, reliable, and portable across different platforms.
	"""
	
	homepage = "https://stringx.gagolewski.com/"
	cran = "stringx" 

	version("0.2.6", md5="ff1c00893303a31d20a47b3183b9d328")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stringi@1.7.2:", type=("build", "run"))
