# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSchtools(RPackage):
	"""Schloss Lab Tools for Reproducible Microbiome Research

	A collection of useful functions and example code created and
    used by the Schloss Lab for reproducible microbiome research. Perform
    common tasks like read files created by mothur <https://mothur.org/>,
    tidy up your microbiome data, and format R Markdown documents for
    publication.  See the website <http://www.schlosslab.org/schtools/>
    for more information, documentation, and examples.
	"""
	
	homepage = "http://www.schlosslab.org/schtools/"
	cran = "schtools" 

	version("0.4.1", md5="49fe3b81f6491acbd193528aec79dd24")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-formatr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
