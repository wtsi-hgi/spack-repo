# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZtree(RPackage):
	"""Functions to Import Data from 'z-Tree' into R

	Read '.xls' and '.sbj' files which are written by the
   Microsoft Windows program 'z-Tree'. The latter is a software for
   developing and carrying out economic experiments
   (see <http://www.ztree.uzh.ch/> for more information).
	"""
	
	cran = "zTree" 

	version("1.0.7", md5="ef7ec3d28753f147de892d0b38d5db3e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr@1:", type=("build", "run"))
