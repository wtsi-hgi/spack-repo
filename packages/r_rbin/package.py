# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbin(RPackage):
	"""Tools for Binning Data

	Manually bin data using weight of evidence and information value. Includes other binning 
    methods such as equal length, quantile and winsorized. Options for combining levels of categorical
    data are also available. Dummy variables can be generated based on the bins created using any of 
    the available binning methods. References: Siddiqi, N. (2006) <doi:10.1002/9781119201731.biblio>.
	"""
	
	homepage = "https://github.com/rsquaredacademy/rbin"
	cran = "rbin" 

	version("0.2.0", md5="508164b012a8101ee6b000e93e6ca16a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
