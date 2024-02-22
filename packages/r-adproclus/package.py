# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdproclus(RPackage):
	"""Additive Profile Clustering Algorithms

	Obtain overlapping clustering models for object-by-variable data
        matrices using the Additive Profile Clustering (ADPROCLUS) method. 
        Also contains the low dimensional ADPROCLUS method 
        for simultaneous dimension reduction and overlapping clustering. 
        For reference see Depril, Van Mechelen, Mirkin (2008) 
        <doi:10.1016/j.csda.2008.04.014> and Depril, Van Mechelen, Wilderjans 
        (2012) <doi:10.1007/s00357-012-9112-5>.
	"""
	
	homepage = "https://github.com/henry-heppe/adproclus"
	cran = "adproclus" 

	version("1.0.2", md5="b12b0468436cb3e2cfd2ae5c8b7b135c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-nmfn", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
