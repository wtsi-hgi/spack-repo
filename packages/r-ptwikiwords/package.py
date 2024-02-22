# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPtwikiwords(RPackage):
	"""Words Used in Portuguese Wikipedia

	Contains a dataset of words used in 15.000 randomly extracted pages
    from the Portuguese Wikipedia (<https://pt.wikipedia.org/>).
	"""
	
	homepage = "https://github.com/dfalbel/ptwikiwords"
	cran = "ptwikiwords" 

	version("0.0.3", md5="17f36fbe98af423b77e867fa716e01e6")

	depends_on("r@3.1:", type=("build", "run"))
