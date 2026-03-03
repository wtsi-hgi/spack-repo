# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsm(RPackage):
	"""Response-Surface Analysis

	Provides functions to generate response-surface designs, 
    fit first- and second-order response-surface models, 
    make surface plots, obtain the path of steepest ascent, 
    and do canonical analysis. A good reference on these methods 
    is Chapter 10 of Wu, C-F J and Hamada, M (2009) 
    "Experiments: Planning, Analysis, and Parameter Design Optimization"
    ISBN 978-0-471-69946-0. An early version of the package is
    documented in Journal of Statistical Software <doi:10.18637/jss.v032.i07>.
	"""
	
	cran = "rsm" 

	version("2.10.4", md5="2d35944cadf6049288e007592868015c")

	depends_on("r-estimability", type=("build", "run"))
