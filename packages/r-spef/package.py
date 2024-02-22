# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpef(RPackage):
	"""Semiparametric Estimating Functions

	Functions for fitting semiparametric regression models for
        panel count survival data. An overview of the package can be found 
        in Wang and Yan (2011) <doi:10.1016/j.cmpb.2010.10.005> and
	Chiou et al. (2018) <doi:10.1111/insr.12271>.
	"""
	
	homepage = "http://github.com/stc04003/spef"
	cran = "spef" 

	version("1.0.9", md5="de791f6232eca4abfa3cfaed4a93a8b7")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
	depends_on("r-squarem", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-sm", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
