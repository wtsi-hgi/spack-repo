# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoscorecard(RPackage):
	"""Fully Automatic Generation of Scorecards

	
    Provides an efficient suite of R tools for scorecard modeling, analysis, and visualization. 
    Including equal frequency binning, equidistant binning, 
    K-means binning, chi-square binning, decision tree binning, data screening, manual parameter modeling, 
    fully automatic generation of scorecards, etc. 
    This package is designed to make scorecard development easier and faster.
    References include:
    1. <http://shichen.name/posts/>. 
    2. Dong-feng Li(Peking University),Class PPT.
    3. <https://zhuanlan.zhihu.com/p/389710022>. 
    4. <https://www.zhangshengrong.com/p/281oqR9JNw/>. 
	"""
	
	cran = "autoScorecard" 

	version("0.3.0", md5="50c343c38dd32a7f332456c055b2813d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-discretization", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
