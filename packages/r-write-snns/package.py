# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWriteSnns(RPackage):
	"""Function for exporting data to SNNS pattern files

	Function for writing a SNNS pattern file from a data.frame
        or matrix.
	"""
	
	cran = "write.snns" 

	version("0.0-4.2", md5="ab2cdf49956f1dd0e201ff643926c01b")

