# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKpodclustr(RPackage):
	"""Method for Clustering Partially Observed Data

	Software for k-means clustering of partially 
    observed data from Chi, Chi, and Baraniuk (2016) <doi:10.1080/00031305.2015.1086685>.
	"""
	
	homepage = "http://jocelynchi.com/kpodclustr"
	cran = "kpodclustr" 

	version("1.1", md5="da51fe1362e5d9ed6d7996831fd9c019")

	depends_on("r@3.1:", type=("build", "run"))
