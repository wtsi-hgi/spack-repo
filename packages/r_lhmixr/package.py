# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLhmixr(RPackage):
	"""Fit Sex-Specific Life History Models with Missing
Classifications

	Fits sex-specific life-history models for fish and other taxa where some of the individuals have unknown sex.
	"""
	
	homepage = "https://github.com/mintoc/lhmixr"
	cran = "lhmixr" 

	version("0.1.0", md5="be842901dedba0e56c89d3e1e9a54c00")

	depends_on("r@3.2:", type=("build", "run"))
