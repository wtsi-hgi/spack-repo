# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRFilesets(RPackage):
	"""Easy Handling of and Access to Files Organized in Structured
Directories

	A file set refers to a set of files located in one or more directories on the file system.  This package provides classes and methods to locate, setup, subset, navigate and iterate such sets.  The API is designed such that these classes can be extended via inheritance to provide a richer API for special file formats.  Moreover, a specific name format is defined such that filenames and directories can be considered to have full names which consists of a name followed by comma-separated tags.  This adds additional flexibility to identify file sets and individual files.  NOTE: This package's API should be considered to be in an beta stage.  Its main purpose is currently to support the aroma.* packages, where it is one of the main core components; if you decide to build on top of this package, please contact the author first.
	"""
	
	homepage = "https://github.com/HenrikBengtsson/R.filesets"
	cran = "R.filesets" 

	version("2.15.1", md5="3c24939c1a510243d2cfc66f724f3842")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r-oo@1.24:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
