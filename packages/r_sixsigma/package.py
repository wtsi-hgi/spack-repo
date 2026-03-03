# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSixsigma(RPackage):
	"""Six Sigma Tools for Quality Control and Improvement

	Functions and utilities to perform
    Statistical Analyses in the Six Sigma way.
    Through the DMAIC cycle (Define, Measure, Analyze, Improve, Control),
    you can manage several Quality Management studies:
    Gage R&R, Capability Analysis, Control Charts, Loss Function Analysis,
    etc. Data frames used in the books "Six Sigma with R" [ISBN 978-1-4614-3652-2]
    and "Quality Control with R" [ISBN 978-3-319-24046-6], 
    are also included in the package.
	"""
	
	homepage = "https://www.sixsigmawithr.com/"
	cran = "SixSigma" 

	version("0.11.1", md5="d598387063562c4f8e78efb5d0732506")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-nortest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
