# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTastypie(RPackage):
	"""Easy Pie Charts

	You only need to type 'why pie charts are bad' on Google to find
    thousands of articles full of (valid) reasons why other types of charts 
    should be preferred over this one.
    Therefore, because of the little use due to the reasons already mentioned,
    making pie charts (and related) in R is not straightforward, so other 
    functions are needed to simplify things.
    In this R package there are useful functions to make 'tasty' pie charts 
    immediately by exploiting the many cool templates provided.
	"""
	
	homepage = "https://paolodalena.github.io/tastypie/"
	cran = "tastypie" 

	version("0.1.1", md5="d4a4415684f8ad94f02d7dc6b1b756bc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-shadowtext", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-packcircles", type=("build", "run"))
	depends_on("r-fmsb", type=("build", "run"))
