# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrake(RPackage):
	"""A Pipeline Toolkit for Reproducible Computation at Scale

	A general-purpose computational engine for data
  analysis, drake rebuilds intermediate data objects when their
  dependencies change, and it skips work when the results are already up
  to date.  Not every execution starts from scratch, there is native
  support for parallel and distributed computing, and completed projects
  have tangible evidence that they are reproducible.  Extensive
  documentation, from beginner-friendly tutorials to practical examples
  and more, is available at the reference website
  <https://docs.ropensci.org/drake/> and the online manual
  <https://books.ropensci.org/drake/>.
	"""
	
	homepage = "https://github.com/ropensci/drake"
	cran = "drake" 

	version("7.13.9", md5="f26b7f07b69a0511569e751b26b7250e")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-base64url", type=("build", "run"))
	depends_on("r-digest@0.6.21:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-storr@1.1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-txtq@0.2.3:", type=("build", "run"))
	depends_on("r-vctrs@0.2:", type=("build", "run"))
