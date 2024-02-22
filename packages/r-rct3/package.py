# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRct3(RPackage):
	"""Predict Fish Year-Class Strength from Survey Data

	Predict fish year-class strength by calibration
  regression analysis of multiple recruitment index series.
	"""
	
	cran = "rct3" 

	version("1.0.4", md5="f8799e0bcc0173015c5cc8d82b38c45b", url="https://cran.r-project.org/src/contrib/rct3_1.0.4.tar.gz")

