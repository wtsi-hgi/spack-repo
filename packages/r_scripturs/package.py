# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScripturs(RPackage):
	"""Complete Text of the LDS Scriptures

	Full text, in data frames containing one row per verse, of the 
    Standard Works of The Church of Jesus Christ of Latter-day Saints (LDS). 
    These are the Old Testament, (KJV), the New Testament (KJV), the Book of 
    Mormon, the Doctrine and Covenants, and the Pearl of Great Price.
	"""
	
	homepage = "https://github.com/andrewheiss/scriptuRs"
	cran = "scriptuRs" 

	version("0.1.0", md5="b1ab6a4b2f7aef2965df8cddc3dcf7c7")

	depends_on("r@3:", type=("build", "run"))
