# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathfindrData(RPackage):
	"""Data Package for 'pathfindR'

	This is a data-only package, containing data needed to run the CRAN 
    package 'pathfindR', a package for enrichment analysis utilizing active 
    subnetworks. This package contains protein-protein interaction network data, 
    data related to gene sets and example input/output data.
	"""
	
	homepage = "https://github.com/egeulgen/pathfindR.data"
	cran = "pathfindR.data" 

	version("2.0.0", md5="407aeb0f07a3e66684504f292939c126")

	depends_on("r@4:", type=("build", "run"))
