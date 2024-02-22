# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvcomp(RPackage):
	"""Performance Assessment and Comparison for Survival Analysis

	Assessment and Comparison for Performance of Risk Prediction (Survival) Models.
	"""
	
	homepage = "http://www.pmgenomics.ca/bhklab/"
	bioc = "survcomp" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/survcomp_1.52.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/survcomp/survcomp_1.52.0.tar.gz"]

	version("1.52.0", md5="5026589c50042751474d3474dc24847d")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-suppdists", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-survivalroc", type=("build", "run"))
	depends_on("r-bootstrap", type=("build", "run"))
	depends_on("r-rmeta", type=("build", "run"))
