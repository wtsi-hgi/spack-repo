# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRequirements(RPackage):
	"""Helper Package to Install Packages for R

	Helper function to install packages for R using an external
    'requirements.txt' or a string containing diverse packages from
    several resources like Github or CRAN.
	"""
	
	homepage = "https://github.com/joundso/requirements"
	cran = "requiRements" 

	version("0.0.3", md5="c654e0a953794a2e4c42dbf8d5ae89f8")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
