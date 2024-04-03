# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtwrappers2(RPackage):
	"""Extensions of 'DTwrappers'

	Offers functionality which provides methods for data analyses and cleaning that can be flexibly applied across multiple variables and in groups. These include cleaning accidental text, contingent calculations, counting missing data, and building summarizations of the data.
	"""
	
	cran = "DTwrappers2" 

	version("0.0.2", md5="17223294435886e8fe4c4376827c969b", url="https://cran.r-project.org/src/contrib/DTwrappers2_0.0.2.tar.gz")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dtwrappers", type=("build", "run"))
