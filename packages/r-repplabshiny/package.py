# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepplabshiny(RPackage):
	"""'REPPlab' via a Shiny Application

	Performs exploratory projection pursuit  via 'REPPlab' (Daniel Fischer, Alain Berro, Klaus Nordhausen & Anne Ruiz-Gazen (2019) <doi:10.1080/03610918.2019.1626880>) using a Shiny app.
	"""
	
	cran = "REPPlabShiny" 

	version("0.4.2", md5="b9548c17e2a022809c0761f50a476d7a")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-repplab", type=("build", "run"))
