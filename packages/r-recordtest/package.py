# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRecordtest(RPackage):
	"""Inference Tools in Time Series Based on Record Statistics

	Statistical tools based on the probabilistic properties of the 
  record occurrence in a sequence of independent and identically distributed 
  continuous random variables. In particular, tools to prepare a time series 
  as well as distribution-free trend and change-point tests and graphical 
  tools to study the record occurrence. Details about the implemented tools 
  can be found in Castillo-Mateo et al. (2023a) <doi:10.18637/jss.v106.i05> 
  and Castillo-Mateo et al. (2023b) <doi:10.1016/j.atmosres.2023.106934>.
	"""
	
	homepage = "https://github.com/JorgeCastilloMateo/RecordTest"
	cran = "RecordTest" 

	version("2.2.0", md5="c4e2837ba46f63e04225da9a2b15c2c6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
