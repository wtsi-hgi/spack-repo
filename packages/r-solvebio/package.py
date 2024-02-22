# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSolvebio(RPackage):
	"""The Official SolveBio API Client

	R language bindings for SolveBio's API.
    SolveBio is a biomedical knowledge hub that enables life science
    organizations to collect and harmonize the complex, disparate
    "multi-omic" data essential for today's R&D and BI needs.
    For more information, visit <https://www.solvebio.com>.
	"""
	
	homepage = "https://github.com/solvebio/solvebio-r"
	cran = "solvebio" 

	version("2.14.0", md5="87b7ab637ad780335b1b6f39808dede9")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-mime", type=("build", "run"))
