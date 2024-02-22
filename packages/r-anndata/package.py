# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnndata(RPackage):
	"""'anndata' for R

	A 'reticulate' wrapper for the Python package 'anndata'.
    Provides a scalable way of keeping track of data and learned
    annotations.  Used to read from and write to the h5ad file format.
	"""
	
	homepage = "https://anndata.dynverse.org"
	cran = "anndata" 

	version("0.7.5.6", md5="450cf5a8850fa79e7586363806de99da")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-reticulate@1.17:", type=("build", "run"))
