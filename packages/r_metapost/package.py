# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetapost(RPackage):
	"""Interface to 'MetaPost'

	Provides an interface to 'MetaPost' (Hobby, 1998) 
    <http://www.tug.org/docs/metapost/mpman.pdf>.
    There are functions to generate an R description of a 'MetaPost'
    curve, functions to generate 'MetaPost' code from an R description,
    functions to process 'MetaPost' code, and functions to read
    solved 'MetaPost' paths back into R.
	"""
	
	homepage = "https://github.com/pmur002/metapost"
	cran = "metapost" 

	version("1.0-6", md5="64dfd69c1d59b9837a5f190bb43a7dd1")

	depends_on("r-gridbezier", type=("build", "run"))
