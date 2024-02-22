# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeducorrect(RPackage):
	"""Deductive Correction, Deductive Imputation, and Deterministic
Correction

	A collection of methods for automated data cleaning where all actions are logged.
	"""
	
	homepage = "https://github.com/data-cleaning/deducorrect"
	cran = "deducorrect" 

	version("1.3.7", md5="7293714bade6233a8b6f23c7a828c9d7")

	depends_on("r-editrules@2.9:", type=("build", "run"))
