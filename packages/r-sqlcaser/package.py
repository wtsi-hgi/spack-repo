# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlcaser(RPackage):
	"""'SQL' Case Statement Generator

	Includes built-in methods for generating long 'SQL' CASE statements,
             and other 'SQL' statements that may otherwise be arduous to construct
             by hand. The generated statement can easily be concatenated to string
             literals to form queries to 'SQL'-like databases, such as when using 
             the 'RODBC' package. The current methods include casewhen() for building 
             CASE statements, inlist() for building IN statements, and
             updatetable() for building UPDATE statements.
	"""
	
	cran = "sqlcaser" 

	version("0.2.0", md5="d812f657526ca9b5bdc96fc2f0a23606")

