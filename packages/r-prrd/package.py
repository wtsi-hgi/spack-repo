# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrrd(RPackage):
	"""Parallel Runs of Reverse Depends

	Reverse depends for a given package are queued such that multiple
 workers can run the reverse-dependency tests in parallel.
	"""
	
	homepage = "https://github.com/eddelbuettel/prrd"
	cran = "prrd" 

	version("0.0.6", md5="1dccf8446ddccf7f4979855bf1a1947f")
	version("0.0.5", md5="5b1a05406bf02260b5a9cc577b2f9654")

	depends_on("r-config", type=("build", "run"))
	depends_on("r-liteq", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
