# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnvd3(RPackage):
	"""An Incomplete Wrapper of the 'nvd3' JavaScript Library

	Creates JavaScript charts with the 'nvd3' library. So far only the multibar chart, the horizontal multibar chart, the line chart and the line chart with focus are available.
	"""
	
	homepage = "https://github.com/stla/Rnvd3"
	cran = "Rnvd3" 

	version("1.0.0", md5="f485b88e170756dbcaaa0384b85eaa8e", url="https://cran.r-project.org/src/contrib/Rnvd3_1.0.0.tar.gz")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-viridislite", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
