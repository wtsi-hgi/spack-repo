# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhymer(RPackage):
	"""Wrapper for the 'Datamuse' API to Find Rhyming and Associated
Words

	Wrapper for 'Datamuse' API to find rhyming and other associated words.
    This includes words of similar meaning, spelling, or other related words. Learn
    more about the 'Datamuse' API here <https://www.datamuse.com/api/>.
	"""
	
	homepage = "https://landesbergn.github.io/rhymer/index.html"
	cran = "rhymer" 

	version("1.2.0", md5="9f2607acb437460e9b416fad67e29373")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
