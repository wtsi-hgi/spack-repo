# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGanpadata(RPackage):
	"""The GANPA Datasets Package

	This is a dataset package for GANPA, which implements a
        network-based gene weighting approach to pathway analysis. This
        package includes data useful for GANPA, such as a functional
        association network, pathways, an expression dataset and
        multi-subunit proteins.
	"""
	
	cran = "GANPAdata" 

	version("1.0", md5="4f3eac55317a69cc7cf912bbb5270a51")

	depends_on("r@2.10:", type=("build", "run"))
