# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiw(RPackage):
	"""Watch the CRAN Incoming Directories

	Directory reads and summaries are provided for one or more of the subdirectories
 of the <https://cran.r-project.org/incoming/> directory, and a compact summary object is returned.
 The package name is a contraption of 'CRAN Incoming Watcher'.
	"""
	
	homepage = "https://github.com/eddelbuettel/ciw"
	cran = "ciw" 

	version("0.0.1", md5="ff73b9e57c3084c51a50ff6016daa561")
	version("0.0.2", md5="0a29bd77081d37ef87d3106dee2bb37b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-data-table@1.5:", type=("build", "run"))
