# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetalite(RPackage):
	"""ADaM Metadata Structure

	A metadata structure for clinical data analysis
    and reporting based on Analysis Data Model (ADaM) datasets.
    The package simplifies clinical analysis and reporting tool development
    by defining standardized inputs, outputs, and workflow.
    The package can be used to create analysis and reporting planning grid,
    mock table, and validated analysis and reporting results based on
    consistent inputs.
	"""
	
	homepage = "https://merck.github.io/metalite/"
	cran = "metalite" 

	version("0.1.3", md5="aab353e60f5de39707c20f75aa27a97c")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
