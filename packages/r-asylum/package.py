# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsylum(RPackage):
	"""Data on Asylum and Resettlement for the UK

	Data on Asylum and Resettlement for the UK,
    provided by the Home Office <https://www.gov.uk/government/statistical-data-sets/immigration-system-statistics-data-tables>.
	"""
	
	homepage = "https://github.com/humaniverse/asylum"
	cran = "asylum" 

	version("1.1.2", md5="48be21fb53997729718d5a98dae1296d")

	depends_on("r@2.10:", type=("build", "run"))
