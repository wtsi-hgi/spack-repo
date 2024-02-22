# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHds(RPackage):
	"""Hazard Discrimination Summary

	Functions for calculating the hazard discrimination summary and its
    standard errors, as described in Liang and Heagerty (2016) <doi:10.1111/biom.12628>.
	"""
	
	homepage = "https://github.com/liangcj/hds"
	cran = "hds" 

	version("0.8.1", md5="e8d7b161dd256597878a0a890ac9233b")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
