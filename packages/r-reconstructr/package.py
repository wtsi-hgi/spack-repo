# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReconstructr(RPackage):
	"""Session Reconstruction and Analysis

	Functions to reconstruct sessions from web log or other user trace data
             and calculate various metrics around them, producing tabular,
             output that is compatible with 'dplyr' or 'data.table' centered processes.
	"""
	
	homepage = "https://github.com/Ironholds/reconstructr"
	cran = "reconstructr" 

	version("2.0.4", md5="9e6ced9251ac10b68641c29b5bfbb672")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-openssl", type=("build", "run"))
