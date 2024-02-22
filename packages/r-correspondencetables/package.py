# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrespondencetables(RPackage):
	"""Creating Correspondence Tables Between Two Statistical
Classifications

	
    A candidate correspondence table between two classifications can be created when there are correspondence tables leading from the first classification to the second one via intermediate 'pivot' classifications. 
    The correspondence table between two statistical classifications can be updated when one of the classifications gets updated to a new version.
	"""
	
	homepage = "https://github.com/eurostat/correspondenceTables"
	cran = "correspondenceTables" 

	version("0.7.4", md5="02d35bc9f5e713c26ca2f438839d3124")

	depends_on("r-data-table", type=("build", "run"))
