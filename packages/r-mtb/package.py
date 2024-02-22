# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMtb(RPackage):
	"""My Toolbox for Assisting Document Editing and Data Presenting

	
    The purpose of this package is to share a collection of functions the author wrote during weekends for managing
    kitchen and garden tasks, e.g. making plant growth charts or Thanksgiving kitchen schedule charts, etc. 
    Functions might include but not limited to:
    (1) aiding summarizing time related data; 
    (2) generating axis transformation from data; and
    (3) aiding Markdown (with html output) and Shiny file editing.
	"""
	
	homepage = "https://github.com/yh202109/mtb"
	cran = "mtb" 

	version("0.1.8", md5="72c3997edc8b8ff7ed842770a378d8c6")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-htmltools@0.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-scales@1:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-labeling@0.3:", type=("build", "run"))
