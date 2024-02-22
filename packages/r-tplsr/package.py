# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTplsr(RPackage):
	"""Thresholded Partial Least Squares Model for Neuroimaging Data

	Uses thresholded partial least squares algorithm to create a regression or classification model. For more information, see Lee, Bradlow, and Kable <doi:10.1016/j.crmeth.2022.100227>.
	"""
	
	cran = "TPLSr" 

	version("1.0.4", md5="ac1368a6e0973be38fc8d93113fb449c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-plotly@4.9.2.1:", type=("build", "run"))
