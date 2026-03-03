# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRandomuseragent(RPackage):
	"""Filtering and Randomly Sampling Real User-Agent Strings

	Based on data of real user-agent strings, we can set filtering conditions
    and randomly sample user-agent strings from the user-agent string pool.
	"""
	
	homepage = "https://github.com/fangzhou-xie/Randomuseragent"
	cran = "Randomuseragent" 

	version("0.0.1", md5="f34d05a1ae58becff46baad0a10e0b33")

	depends_on("r@3.5:", type=("build", "run"))
