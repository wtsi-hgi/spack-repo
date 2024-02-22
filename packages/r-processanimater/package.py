# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProcessanimater(RPackage):
	"""Process Map Token Replay Animation

	Provides animated process maps based on the 'procesmapR' package.
  Cases stored in event logs created with with 'bupaR' S3 class eventlog() are
  rendered as tokens (SVG shapes) and animated according to their occurrence 
  times on top of the process map. For rendering SVG animations ('SMIL') and the
  'htmlwidget' package are used.
	"""
	
	homepage = "https://github.com/bupaverse/processanimateR/"
	cran = "processanimateR" 

	version("1.0.5", md5="dcc17930dc2413bccee162d072a72a44")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-bupar", type=("build", "run"))
	depends_on("r-processmapr@0.3.1:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
