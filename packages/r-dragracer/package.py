# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDragracer(RPackage):
	"""Data Sets for RuPaul's Drag Race

	These are data sets for the hit TV show, RuPaul's Drag Race. 
    Data right now include episode-level data, contestant-level data, and 
    episode-contestant-level data. This is a work in progress, and a love letter
    of a kind to RuPaul's Drag Race and the performers that have appeared on the show.
    This may not be the most productive use of my time, but I have tenure and what 
    are you going to do about it? I think there is at least some value in this package
    if it allows the show's fandom to learn more about the R programming language 
    around its contents.
	"""
	
	cran = "dragracer" 

	version("0.1.7", md5="d425ed8b88aa07fe7dc8c71ca25fd376")

	depends_on("r@3.5:", type=("build", "run"))
