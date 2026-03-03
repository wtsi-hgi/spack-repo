# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrqa(RPackage):
	"""Unidimensional and Multidimensional Methods for Recurrence
Quantification Analysis

	
    Auto, Cross and Multi-dimensional recurrence quantification analysis. 
    Different methods for computing recurrence, cross vs. multidimensional
    or profile iti.e., only looking at the diagonal recurrent points, 
    as well as functions for optimization and plotting are proposed.
    in-depth measures of the whole cross-recurrence plot,
    Please refer to Coco and others (2021) <doi:10.32614/RJ-2021-062>,
    Coco and Dale (2014) <doi:10.3389/fpsyg.2014.00510> 
    and Wallot (2018) <doi: 10.1080/00273171.2018.1512846>
    for further details about the method.
	"""
	
	cran = "crqa" 

	version("2.0.5", md5="28201d0176298504b3f4efaad83e002a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-tserieschaos", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-rdist", type=("build", "run"))
