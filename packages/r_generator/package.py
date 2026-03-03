# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenerator(RPackage):
	"""Generate Data Containing Fake Personally Identifiable
Information

	Allows users to quickly and easily generate fake data containing
    Personally Identifiable Information (PII) through convenience functions.
	"""
	
	homepage = "https://github.com/paulhendricks/generator"
	cran = "generator" 

	version("0.1.0", md5="8303be0006ae3b02e337e25774c709da")

	depends_on("r@3.1.2:", type=("build", "run"))
