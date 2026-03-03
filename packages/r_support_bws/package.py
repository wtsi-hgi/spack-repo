# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSupportBws(RPackage):
	"""Tools for Case 1 Best-Worst Scaling

	Provides basic functions that support an implementation of object case (Case 1) best-worst scaling: a function for converting a two-level orthogonal main-effect design/balanced incomplete block design into questions; two functions for creating a data set suitable for analysis; a function for calculating count-based scores; a function for calculating shares of preference; and a function for generating artificial responses to questions. See Louviere et al. (2015) <doi:10.1017/CBO9781107337855> for details on best-worst scaling, and Aizaki and Fogarty (2023) <doi:10.1016/j.jocm.2022.100394> for the package.
	"""
	
	homepage = "http://lab.agr.hokudai.ac.jp/spmur/"
	cran = "support.BWS" 

	version("0.4-6", md5="aa568e6e382508d6111900674225c544")

