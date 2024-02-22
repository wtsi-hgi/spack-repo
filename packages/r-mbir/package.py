# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbir(RPackage):
	"""Magnitude-Based Inferences

	Allows practitioners and researchers a wholesale approach for deriving magnitude-based inferences from raw data. A major goal of 'mbir' is to programmatically detect appropriate statistical tests to run in lieu of relying on practitioners to determine correct stepwise procedures independently.
	"""
	
	homepage = "http://mbir-project.us/"
	cran = "mbir" 

	version("1.3.5", md5="6803fa2312cb80d741fe4af19b7624bf")

	depends_on("r-effsize", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
