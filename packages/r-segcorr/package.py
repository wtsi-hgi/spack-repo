# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegcorr(RPackage):
	"""Detecting Correlated Genomic Regions

	Performs correlation matrix segmentation and applies a test
    procedure to detect highly correlated regions in gene expression.
	"""
	
	cran = "SegCorr" 

	version("1.2", md5="a5ec2fb5340a1fc38c04922a7ecbb4e1")

	depends_on("r-jointseg", type=("build", "run"))
