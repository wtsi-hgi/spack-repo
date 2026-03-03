# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmicsense(RPackage):
	"""Biosensor Development using Omics Data

	A method for the quantitative prediction using omics data. 
    This package provides functions to construct the quantitative prediction 
    model using omics data. 
	"""
	
	homepage = "<https://github.com/takakoizumi/OmicSense>"
	cran = "OmicSense" 

	version("0.2.0", md5="bba1d5d66cfe121f315e3b65ed951dab")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
