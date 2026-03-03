# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYmd(RPackage):
	"""Parse 'YMD' Format Number or String to Date

	Convert 'YMD' format number or string to Date efficiently, using Rust's
    standard library. It also provides helper functions to handle Date, e.g., quick
    finding the beginning or end of the given period, adding months to Date, etc.
	"""
	
	homepage = "https://shrektan.github.io/ymd/"
	cran = "ymd" 

	version("0.1.0", md5="bf0b6e91bca823e37c403790527d0474")

	depends_on("rust", type=("build", "link", "run"))
