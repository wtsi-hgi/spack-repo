# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecommenderlabbx(RPackage):
	"""Book-Crossing Dataset (BX) for 'recommenderlab'

	Provides the Book-Crossing Dataset for the package recommenderlab.
	"""
	
	homepage = "https://github.com/mhahsler/recommenderlabBX"
	cran = "recommenderlabBX" 

	version("0.2-0", md5="b6cb31b4ad8fcc45099255a13a01f532")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-recommenderlab@1.0.0:", type=("build", "run"))
