# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REchelon(RPackage):
	"""The Echelon Analysis and the Detection of Spatial Clusters using
Echelon Scan Method

	Functions for the echelon analysis proposed by Myers et al. (1997) <doi:10.1023/A:1018518327329>, and the detection of spatial clusters using echelon scan method proposed by Kurihara (2003) <doi:10.20551/jscswabun.15.2_171>.
	"""
	
	cran = "echelon" 

	version("0.2.0", md5="040e32089a3df285456be1b241c529b2")

	depends_on("r@3.3:", type=("build", "run"))
