# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSgp(RPackage):
	"""Student Growth Percentiles & Percentile Growth Trajectories

	An analytic framework for the calculation of norm- and criterion-referenced academic growth estimates using large scale, longitudinal education assessment data as developed in Betebenner (2009) <doi:10.1111/j.1745-3992.2009.00161.x>.
	"""
	
	homepage = "https://sgp.io"
	cran = "SGP" 

	version("2.1-0.0", md5="bc2fb949400e6b22dc567311e9d03a9b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cairo", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-data-table@1.14:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-equate@2.0.5:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-randomnames@0.0.5:", type=("build", "run"))
	depends_on("r-rngtools@1.5:", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-sn@1.0.0:", type=("build", "run"))
	depends_on("r-svglite", type=("build", "run"))
	depends_on("r-toordinal", type=("build", "run"))
