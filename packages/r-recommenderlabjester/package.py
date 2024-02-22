# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecommenderlabjester(RPackage):
	"""Jester Dataset for 'recommenderlab'

	Provides the Jester Dataset for package recommenderlab.
	"""
	
	homepage = "https://github.com/mhahsler/recommenderlabJester"
	cran = "recommenderlabJester" 

	version("0.2-0", md5="ea79a3b802e80d419b9558194bc2cb5e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-recommenderlab@1:", type=("build", "run"))
