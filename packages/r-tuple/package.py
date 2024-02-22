# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTuple(RPackage):
	"""Find every match, or orphan, duplicate, triplicate, or other
replicated values

	Functions to find all matches or non-matches, orphans, and
    duplicate or other replicated elements.
	"""
	
	homepage = "http://statistics.lazaridis.eu"
	cran = "tuple" 

	version("0.4-02", md5="074ff152ddf852cd709a50d56ba0e7ad")

	depends_on("r@2.10:", type=("build", "run"))
