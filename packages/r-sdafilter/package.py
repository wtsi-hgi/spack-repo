# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdafilter(RPackage):
	"""Symmetrized Data Aggregation

	We develop a new class of distribution free multiple testing rules for false discovery rate (FDR) control under general dependence. A key element in our proposal is a symmetrized data aggregation (SDA) approach to incorporating the dependence structure via sample splitting, data screening and information pooling. The proposed SDA filter first constructs a sequence of ranking statistics that fulfill global symmetry properties, and then chooses a data driven threshold along the ranking to control the FDR. For more information, see the website below and the accompanying paper: Du et al. (2020), "False Discovery Rate Control Under General Dependence By Symmetrized Data Aggregation", <arXiv:2002.11992>.
	"""
	
	cran = "sdafilter" 

	version("1.0.0", md5="48f5362e562e5d7257201aa187ed5fe0")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-glasso", type=("build", "run"))
	depends_on("r-huge", type=("build", "run"))
	depends_on("r-poet", type=("build", "run"))
