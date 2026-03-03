# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGt4ireval(RPackage):
	"""Generalizability Theory for Information Retrieval Evaluation

	Provides tools to measure the reliability of an Information Retrieval test collection.
  It allows users to estimate reliability using Generalizability Theory and map those estimates onto
  well-known indicators such as Kendall tau correlation or sensitivity.
	"""
	
	homepage = "https://github.com/julian-urbano/gt4ireval/"
	cran = "gt4ireval" 

	version("2.0", md5="effbe443389eeec88639480d7db255a0")

	depends_on("r@3.2:", type=("build", "run"))
