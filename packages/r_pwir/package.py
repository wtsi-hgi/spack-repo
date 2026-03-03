# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwir(RPackage):
	"""Provides a Function to Calculate Prize Winner Indices Based on
Bibliometric Data

	A function 'PWI()' that calculates prize winner indices based on bibliometric data is provided. The default is the 'Derek de Solla Price Memorial Medal'. Users can provide recipients of other prizes.
	"""
	
	cran = "PWIR" 

	version("0.0.3", md5="6822d7a6e46bff0048685b8d237c1620")

	depends_on("r-bibliometrix", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-progressr", type=("build", "run"))
