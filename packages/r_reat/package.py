# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReat(RPackage):
	"""Regional Economic Analysis Toolbox

	Collection of models and analysis methods used in regional and urban economics and (quantitative) economic geography, e.g. measures of inequality, regional disparities and convergence, regional specialization as well as accessibility and spatial interaction models.
	"""
	
	cran = "REAT" 

	version("3.0.3", md5="0807981f6f55758bab021a5686951f46")

