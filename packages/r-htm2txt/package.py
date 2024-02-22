# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtm2txt(RPackage):
	"""Convert Html into Text

	Convert a html document to plain texts by stripping off all html tags.
	"""
	
	homepage = "https://github.com/replicable/htm2txt"
	cran = "htm2txt" 

	version("2.2.2", md5="f24053cecfeaa1a1b32519c08f42888b")

