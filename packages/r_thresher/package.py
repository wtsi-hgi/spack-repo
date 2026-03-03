# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThresher(RPackage):
	"""Threshing and Reaping for Principal Components

	Defines the classes used to identify
  outliers (threshing) and compute the number of significant principal
  components and number of clusters (reaping) in a joint application
  of PCA and hierarchical clustering. See Wang et al., 2018,
  <doi:10.1186/s12859-017-1998-9>.
	"""
	
	homepage = "http://oompa.r-forge.r-project.org/"
	cran = "Thresher" 

	version("1.1.3", md5="dde1533d9b9ab0ebc7a654bb18cf83fb")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-classdiscovery", type=("build", "run"))
	depends_on("r-pcdimension", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-movmf", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-oompabase", type=("build", "run"))
