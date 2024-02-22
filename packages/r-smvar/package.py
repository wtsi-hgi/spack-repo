# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmvar(RPackage):
	"""Structural Model for Variances

	Implementation of the structural model for variances in order to
        detect differentially expressed genes from gene expression data.
	"""
	
	cran = "SMVar" 

	version("1.3.4", md5="0cad7d2abfd4be6306eaf2bce923ce7d")

	depends_on("r@2.6:", type=("build", "run"))
