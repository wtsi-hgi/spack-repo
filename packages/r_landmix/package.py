# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLandmix(RPackage):
	"""Landmark Prediction for Mixture Data

	Non-parametric prediction of survival outcomes for mixture data that incorporates covariates and a landmark time. Details are described in Garcia (2021) <doi:10.1093/biostatistics/kxz052>.
	"""
	
	cran = "landmix" 

	version("1.0", md5="cc6ec438ad575ad2dec288f13636de5e")

