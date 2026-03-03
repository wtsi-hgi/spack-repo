# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSeg(RPackage):
	"""Measuring Spatial Segregation

	Measuring spatial segregation. The methods implemented in this 
        package include White's P index (1983) <doi:10.1086/227768>, 
        Morrill's D(adj) (1991), Wong's D(w) and D(s) (1993) 
        <doi:10.1080/00420989320080551>, and Reardon and O'Sullivan's set of 
        spatial segregation measures (2004) 
        <doi:10.1111/j.0081-1750.2004.00150.x>.
	"""
	
	homepage = "https://github.com/syunhong/seg"
	cran = "seg" 

	version("0.5-7", md5="b473dbe749fd37c67796f84befcc99a5")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-splancs", type=("build", "run"))
