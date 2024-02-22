# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsymetadata(RPackage):
	"""Open Datasets from Meta-Analyses in Psychology Research

	Data and examples from meta-analyses in psychology research. 
	"""
	
	cran = "psymetadata" 

	version("1.0.1", md5="dc16af0d907b56f3e152ca34efc561eb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
