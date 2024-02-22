# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBodenmiller(RPackage):
	"""Profiling of Peripheral Blood Mononuclear Cells using CyTOF

	This data package contains a subset of the Bodenmiller et al, Nat Biotech 2012 dataset for testing single cell, high dimensional analysis and visualization methods.
	"""
	
	homepage = "https://github.com/yannabraham/bodenmiller"
	cran = "bodenmiller" 

	version("0.1.1", md5="305ccb9f1bc856786d007ef2f54e5b06")

	depends_on("r@3.1:", type=("build", "run"))
