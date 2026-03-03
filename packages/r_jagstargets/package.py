# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJagstargets(RPackage):
	"""Targets for JAGS Pipelines

	Bayesian data analysis usually incurs long runtimes
  and cumbersome custom code.
  A pipeline toolkit tailored to Bayesian statisticians,
  the 'jagstargets' R package is leverages
  'targets' and 'R2jags' to ease this burden.
  'jagstargets' makes it super easy to set up scalable
  JAGS pipelines that automatically parallelize the computation
  and skip expensive steps when the results are already up to date.
  Minimal custom code is required, and there is no need to manually
  configure branching, so usage is much easier than 'targets' alone.
  For the underlying methodology, please refer
  to the documentation of 'targets' <doi:10.21105/joss.02959> and 'JAGS'
  (Plummer 2003) <https://www.r-project.org/conferences/DSC-2003/Proceedings/Plummer.pdf>.
	"""
	
	homepage = "https://docs.ropensci.org/jagstargets/"
	cran = "jagstargets" 

	version("1.1.0", md5="18b7e1a7debd82fe2d06ce6e7ba33d6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda@0.19.4:", type=("build", "run"))
	depends_on("r-digest@0.6.25:", type=("build", "run"))
	depends_on("r-fst@0.9.2:", type=("build", "run"))
	depends_on("r-posterior@1.0.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.4:", type=("build", "run"))
	depends_on("r-qs@0.23.2:", type=("build", "run"))
	depends_on("r-r2jags@0.6.1:", type=("build", "run"))
	depends_on("r-rjags@4.10:", type=("build", "run"))
	depends_on("r-rlang@0.4.10:", type=("build", "run"))
	depends_on("r-targets@0.12:", type=("build", "run"))
	depends_on("r-tarchetypes@0.6:", type=("build", "run"))
	depends_on("r-tibble@3.0.1:", type=("build", "run"))
	depends_on("r-withr@2.1.2:", type=("build", "run"))
	depends_on("jags@4.0.0:", type=("build", "link", "run"))
