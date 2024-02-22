# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAidar(RPackage):
	"""Tools for Reading AIDA Files

	Read objects from the AIDA (<http://aida.freehep.org/>) file and make them available as dataframes in R.
	"""
	
	cran = "aidar" 

	version("1.0.5", md5="aa0f8c7a6432ef78e0381d03b7a237e5")

	depends_on("r-xml", type=("build", "run"))
