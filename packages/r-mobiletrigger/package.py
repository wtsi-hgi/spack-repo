# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobiletrigger(RPackage):
	"""Run Reports, Models, and Scripts from a Mobile Device

	A framework for interacting with
  R modules such as Reports, Models, and Scripts from a mobile device. 
  The framework allows you to list available modules and select a
  module of interest using a basic e-mail interface. After 
  selecting a specific module, you can either run it as is or 
  provide input via the e-mail interface. After parsing your
  request, R will send the results back to your mobile device.
	"""
	
	cran = "MobileTrigger" 

	version("0.0.31", md5="b4edfb015a605a8899a2d0a3a97d4643")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-mailr", type=("build", "run"))
