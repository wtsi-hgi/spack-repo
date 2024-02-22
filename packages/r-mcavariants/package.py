# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcavariants(RPackage):
	"""Multiple Correspondence Analysis Variants

	Provides two variants of multiple correspondence analysis (ca):
                     multiple ca and ordered multiple ca via orthogonal polynomials of Emerson.
	"""
	
	homepage = "https://www.R-project.org"
	cran = "MCAvariants" 

	version("2.6.1", md5="c7bbb996dffe6deedc4a1fade1b9bb13")

	depends_on("r@3.0.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
