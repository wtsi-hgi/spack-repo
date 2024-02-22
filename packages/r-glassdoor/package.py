# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlassdoor(RPackage):
	"""Interface to 'Glassdoor' API

	Interacts with the 'Glassdoor' API
    <https://www.glassdoor.com/developer/index.htm>. Allows the user to
    search job statistics, employer statistics, and job progression,
    where 'Glassdoor' provides a breakdown of other jobs a person did
    after their current one.
	"""
	
	cran = "glassdoor" 

	version("0.8.1", md5="77eee17b5ecef2bed93b1b0a0b60bf2e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
