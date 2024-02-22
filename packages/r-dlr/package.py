# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlr(RPackage):
	"""Download and Cache Files Safely

	The goal of dlr is to provide a friendly wrapper around the common 
    pattern of downloading a file if that file does not already exist locally. 
	"""
	
	homepage = "https://github.com/macmillancontentscience/dlr"
	cran = "dlr" 

	version("1.0.1", md5="9509715641c576892ebb47408edd1b78")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
