# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUnvotes(RPackage):
	"""United Nations General Assembly Voting Data

	Historical voting data of the United Nations General Assembly. This
    includes votes for each country in each roll call, as well as descriptions and
    topic classifications for each vote.
	"""
	
	homepage = "https://github.com/dgrtwo/unvotes"
	cran = "unvotes" 

	version("0.3.0", md5="106148cb67eb1701418c992c3531e7e0")

	depends_on("r@2.10:", type=("build", "run"))
