# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResmush(RPackage):
	"""Optimize and Compress Image Files with 'reSmush.it'

	Compress local and online images using the 'reSmush.it' API
    service <https://resmush.it/>.
	"""
	
	homepage = "https://dieghernan.github.io/resmush/"
	cran = "resmush" 

	version("0.1.0", md5="e3f9d3aff4b4e22b3035f4b36eceb78f")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr2@1:", type=("build", "run"))
