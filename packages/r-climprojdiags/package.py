# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClimprojdiags(RPackage):
	"""Set of Tools to Compute Various Climate Indices

	Set of tools to compute metrics and indices for climate analysis.
    The package provides functions to compute extreme indices, evaluate the
    agreement between models and combine theses models into an ensemble. Multi-model
    time series of climate indices can be computed either after averaging the 2-D
    fields from different models provided they share a common grid or by combining
    time series computed on the model native grid. Indices can be assigned weights
    and/or combined to construct new indices.
	"""
	
	homepage = "https://earth.bsc.es/gitlab/es/ClimProjDiags"
	cran = "ClimProjDiags" 

	version("0.3.3", md5="90482f991eabfe806259a87f96ddf1e2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-multiapply@2:", type=("build", "run"))
	depends_on("r-pcict", type=("build", "run"))
