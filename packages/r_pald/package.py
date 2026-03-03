# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPald(RPackage):
	"""Partitioned Local Depth for Community Structure in Data

	Implementation of the Partitioned Local Depth (PaLD) 
    approach which provides a measure of local depth and the cohesion of a point 
    to another which  (together with a universal threshold for distinguishing 
    strong and weak ties) may be used to reveal local and global structure in 
    data, based on methods described in Berenhaut, Moore, and Melvin (2022)
    <doi:10.1073/pnas.2003634119>. No extraneous inputs, distributional 
    assumptions, iterative procedures nor optimization criteria are employed. 
    This package includes functions for computing local depths and cohesion as
    well as flexible functions for plotting community networks and displays of 
    cohesion against distance. 
	"""
	
	homepage = "https://github.com/LucyMcGowan/pald"
	cran = "pald" 

	version("0.0.3", md5="57333aefc9ab686a75ec036d20b986c8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
