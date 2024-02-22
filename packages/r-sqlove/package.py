# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlove(RPackage):
	"""Execute 'SQL' Scripts in 'R' Containing Multiple Queries

	The nature of working with structured query language ('SQL') scripts 
             efficiently often requires the creation of temporary tables and there 
             are few clean and simple 'R' 'SQL' execution approaches that allow 
             you to complete this kind of work with the 'R' environment. This 
             package seeks to give 'SQL' implementations in 'R' a little love 
             by deploying functions that allow you to deploy complex 'SQL' 
             scripts within a typical 'R' workflow.
	"""
	
	cran = "SQLove" 

	version("0.0.4", md5="2358f5f2121697a829dc84382bb45ff2")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rjdbc", type=("build", "run"))
