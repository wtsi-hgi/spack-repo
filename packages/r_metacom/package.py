# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetacom(RPackage):
	"""Analysis of the 'Elements of Metacommunity Structure'

	Functions to analyze coherence, boundary clumping, and turnover
    following the pattern-based metacommunity analysis of Leibold and Mikkelson
    2002  <doi:10.1034/j.1600-0706.2002.970210.x>. The package also includes 
		functions to visualize ecological networks, and to calculate modularity 
		as a replacement to boundary clumping.
	"""
	
	homepage = "https://cran.r-project.org/package=metacom"
	cran = "metacom" 

	version("1.5.3", md5="59aec2094ce8c060ffdc00c4cd7d16bf")

	depends_on("r-vegan@2.2.1:", type=("build", "run"))
