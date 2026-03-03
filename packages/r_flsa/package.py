# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlsa(RPackage):
	"""Path Algorithm for the General Fused Lasso Signal Approximator

	Implements a path algorithm for the Fused Lasso Signal Approximator.
    For more details see the help files or the article by Hoefling (2009) <arXiv:0910.0526>.
	"""
	
	cran = "flsa" 

	version("1.5.5", md5="0b2574da0926874780976e42ed88e58e")

	depends_on("r@2:", type=("build", "run"))
