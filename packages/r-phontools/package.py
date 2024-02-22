# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhontools(RPackage):
	"""Tools for Phonetic and Acoustic Analyses

	Contains tools for the organization, display, and analysis of the sorts of data frequently encountered in phonetics research and experimentation, including the easy creation of IPA vowel plots, and the creation and manipulation of WAVE audio files.
	"""
	
	cran = "phonTools" 

	version("0.2-2.2", md5="87a9b3eb90af99a7ebe181fa3abfe41c")

	depends_on("r@2.15:", type=("build", "run"))
