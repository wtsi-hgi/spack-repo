# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDclusterm(RPackage):
	"""Model-Based Detection of Disease Clusters

	Model-based methods for the detection of disease clusters
  using GLMs, GLMMs and zero-inflated models. These methods are described
  in 'V. Gómez-Rubio et al.' (2019) <doi:10.18637/jss.v090.i14> and
  'V. Gómez-Rubio et al.' (2018) <doi:10.1007/978-3-030-01584-8_1>.
	"""
	
	cran = "DClusterm" 

	version("1.0-1", md5="80deb2587fb69e607169928d2af45f64")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-dcluster", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
