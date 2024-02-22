# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplegraphdb(RPackage):
	"""A Simple Graph Database

	This is a graph database in 'SQLite'.  It is inspired by Denis Papathanasiou's Python simple-graph project on 'GitHub'.
	"""
	
	homepage = "https://github.com/mikeasilva/simplegraphdb"
	cran = "simplegraphdb" 

	version("2021.03.10", md5="ff62b4fbcc319a49dd89a5ac95f30c5a")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
