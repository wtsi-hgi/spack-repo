# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatdat(RPackage):
	"""Portal Project Teaching Database

	A simplified version of the Portal Project Database designed for
    teaching. It provides a real world example of life-history, population, and
    ecological data, with sufficient complexity to teach many aspects of data
    analysis and management, but with many complexities removed to allow
    students to focus on the core ideas and skills being taught. The full
    database (which should be used for research) is available at
    <https://github.com/weecology/PortalData>.
	"""
	
	cran = "ratdat" 

	version("1.1.0", md5="3c84c5d7ee14045303d0fe5814baf63e")

	depends_on("r@3.5:", type=("build", "run"))
