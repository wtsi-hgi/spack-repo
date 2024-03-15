# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGcplyr(RPackage):
	"""Wrangle and Analyze Growth Curve Data

	Easy wrangling and model-free analysis of
    microbial growth curve data, as commonly output by plate readers.
    Tools for reshaping common plate reader outputs into 'tidy' formats and
    merging them with design information, making data easy to work with using 
    'gcplyr' and other packages. Also streamlines common growth curve
    processing steps, like smoothing and calculating derivatives, and
    facilitates model-free characterization and analysis of growth data.
    See methods at <https://mikeblazanin.github.io/gcplyr/>.
	"""
	
	homepage = "https://mikeblazanin.github.io/gcplyr/"
	cran = "gcplyr" 

	version("1.9.0", md5="f55e60ce6fc64f95374589c29bca00c0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
