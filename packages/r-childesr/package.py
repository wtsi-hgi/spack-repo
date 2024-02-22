# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChildesr(RPackage):
	"""Accessing the 'CHILDES' Database

	Tools for connecting to 'CHILDES', an open repository for
    transcripts of parent-child interaction. For more information on the 
    underlying data, see <https://langcog.github.io/childes-db-website/>.
	"""
	
	homepage = "https://github.com/langcog/childesr"
	cran = "childesr" 

	version("0.2.3", md5="475e71face10f694d33b4dc78f65bdbe")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-dbplyr@2.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-magrittr@2:", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rmysql@0.10.21:", type=("build", "run"))
