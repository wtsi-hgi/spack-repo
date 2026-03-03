# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFsadata(RPackage):
	"""Data to Support Fish Stock Assessment ('FSA') Package

	The datasets to support the Fish Stock Assessment ('FSA') package.
	"""
	
	homepage = "https://fishr-core-team.github.io/FSAdata/"
	cran = "FSAdata" 

	version("0.4.1", md5="cab4d10ba78e1197821e9a27a7e51214")

	depends_on("r@3:", type=("build", "run"))
