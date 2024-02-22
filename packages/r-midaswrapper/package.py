# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMidaswrapper(RPackage):
	"""Microcluster-Based Detector of Anomalies in Edge Streams

	This is a wrapper around the C++ implementation of 'MIDAS' (Bhatia et al., 2020) <https://www.comp.nus.edu.sg/~sbhatia/assets/pdf/midas.pdf> by Siddharth Bhatia for graph like data.
	"""
	
	homepage = "https://github.com/pteridin/MIDASwrappeR"
	cran = "MIDASwrappeR" 

	version("0.5.1", md5="9e2397662fb0f330fd394500ce3a92e6")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
