# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJosaplay(RPackage):
	"""Add Josa Based on Previous Letter in Korean

	Josa in Korean is often determined by judging the previous word. 
            When writing reports using Rmd, a function that prints the 
            appropriate investigation for each case is helpful. 
            The 'josaplay' package then evaluates the previous word 
            to determine which josa is appropriate.
	"""
	
	homepage = "https://github.com/mrchypark/josaplay"
	cran = "josaplay" 

	version("0.1.3", md5="9ed79f00f20774cde2a26bfa6f2d58f5")

	depends_on("r-utf8", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
