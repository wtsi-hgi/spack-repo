# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCchsflow(RPackage):
	"""Transforming and Harmonizing CCHS Variables

	Supporting the use of the Canadian Community Health Survey 
             (CCHS) by transforming variables from each cycle into harmonized, 
             consistent versions that span survey cycles (currently, 2001 to 
             2018). CCHS data used in this library is accessed and adapted in 
             accordance to the Statistics Canada Open Licence Agreement. This 
             package uses rec_with_table(), which was developed from 'sjmisc' 
             rec(). Lüdecke D (2018). "sjmisc: Data and Variable Transformation 
             Functions". Journal of Open Source Software, 3(26), 754. 
             <doi:10.21105/joss.00754>.
	"""
	
	homepage = "https://github.com/Big-Life-Lab/cchsflow"
	cran = "cchsflow" 

	version("2.1.0", md5="244b1aeec6569369bce5fa65add5c7e2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-haven@1.1.2:", type=("build", "run"))
	depends_on("r-dplyr@0.8.2:", type=("build", "run"))
	depends_on("r-sjlabelled@1.0.17:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
