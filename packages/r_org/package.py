# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrg(RPackage):
	"""Organising Projects

	A system to help you organize projects. Most analyses have three (or more) main sections: code, results, and data, each with different requirements (version control/sharing/encryption). You provide folder locations and 'org' helps you take care of the details.
	"""
	
	homepage = "https://www.csids.no/org/"
	cran = "org" 

	version("2022.11.23", md5="5535a2efb9b3cdd24c05b5d662acfdf2")

	depends_on("r@3.3:", type=("build", "run"))
