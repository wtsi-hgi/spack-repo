# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnhanes(RPackage):
	"""Facilitates Analysis of CDC NHANES Data

	Tools for downloading and analyzing CDC NHANES data, with a focus
    on analytical laboratory data.
	"""
	
	homepage = "http://github.com/silentspringinstitute/RNHANES"
	cran = "RNHANES" 

	version("1.1.0", md5="985cde110d59eff1a91b7f6a2c1f3940")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
