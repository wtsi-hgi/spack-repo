# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoxytypes(RPackage):
	"""Typed Parameter Tags for Integration with 'roxygen2'

	Provides typed parameter documentation tags for integration
    with 'roxygen2'. Typed parameter tags provide a consistent interface for
    annotating expected types for parameters and returned values. Tools for
    converting from existing styles are also provided to easily adapt projects
    which implement typed documentation by convention rather than tag. Use the
    default format or provide your own.
	"""
	
	homepage = "https://github.com/openpharma/roxytypes"
	cran = "roxytypes" 

	version("0.1.0", md5="e00618a28c82818aa36632bfa2412765")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
