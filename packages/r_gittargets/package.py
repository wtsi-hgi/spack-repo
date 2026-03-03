# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGittargets(RPackage):
	"""Data Version Control for the Targets Package

	In computationally demanding data analysis pipelines,
  the 'targets' R package (2021, <doi:10.21105/joss.02959>) maintains
  an up-to-date set of results while skipping tasks that do not need to rerun.
  This process increases speed and increases trust in the final end product.
  However, it also overwrites old output with new output, and past
  results disappear by default. To preserve historical output, the 'gittargets'
  package captures version-controlled snapshots of the data store,
  and each snapshot links to the underlying commit of the source code.
  That way, when the user rolls back the code to a previous branch or commit,
  'gittargets' can recover the data contemporaneous with that commit so that
  all targets remain up to date.
	"""
	
	homepage = "https://docs.ropensci.org/gittargets/"
	cran = "gittargets" 

	version("0.0.7", md5="a4f3c8e91b868eeed8aaddee8a3b1e43")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-callr@3:", type=("build", "run"))
	depends_on("r-cli@3.1:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-gert@1:", type=("build", "run"))
	depends_on("r-processx@3:", type=("build", "run"))
	depends_on("r-targets@0.6:", type=("build", "run"))
	depends_on("r-tibble@3:", type=("build", "run"))
	depends_on("r-uuid@0.1.4:", type=("build", "run"))
	depends_on("git@2.0.0:", type=("build", "link", "run"))
