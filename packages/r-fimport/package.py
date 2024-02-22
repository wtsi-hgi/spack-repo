# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFimport(RPackage):
	"""Rmetrics - Importing Economic and Financial Data

	Provides a collection of utility functions 
    to download and manage data sets from the Internet or from other 
    sources.
	"""
	
	homepage = "https://r-forge.r-project.org/scm/viewvc.php/pkg/fImport/?root=rmetrics"
	cran = "fImport" 

	version("4032.87", md5="c2db3b61ba9536d358169150841a27fe")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-timedate", type=("build", "run"))
	depends_on("r-timeseries", type=("build", "run"))
