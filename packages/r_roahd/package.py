# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoahd(RPackage):
	"""Robust Analysis of High Dimensional Data

	A collection of methods for the robust analysis of univariate and
    multivariate functional data, possibly in high-dimensional cases, and hence
    with attention to computational efficiency and simplicity of use. See the R 
    Journal publication of Ieva et al. (2019) <doi:10.32614/RJ-2019-032> for an 
    in-depth presentation of the 'roahd' package. See Aleman-Gomez et al. (2021) 
    <arXiv:2103.08874> for details about the concept of depthgram.
	"""
	
	homepage = "https://astamm.github.io/roahd/"
	cran = "roahd" 

	version("1.4.3", md5="3db39f8d70bb16ff2b6356e2711dc33b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
