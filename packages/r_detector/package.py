# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDetector(RPackage):
	"""Detect Data Containing Personally Identifiable Information

	Allows users to quickly and easily detect data containing
    Personally Identifiable Information (PII) through convenience functions.
	"""
	
	homepage = "https://github.com/paulhendricks/detector"
	cran = "detector" 

	version("0.1.0", md5="c061e83b3195425ecc013a831eb5ba9a")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
