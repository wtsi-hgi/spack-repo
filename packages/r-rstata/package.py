# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRstata(RPackage):
	"""A Bit of Glue Between R and Stata

	A simple R -> Stata interface allowing the user to
    execute Stata commands (both inline and from a .do file)
    from R.
	"""
	
	homepage = "http://github.com/lbraglia/RStata"
	cran = "RStata" 

	version("1.1.1", md5="06b3ce0e21dbf760eb322afe7413755e")

	depends_on("r-foreign", type=("build", "run"))
