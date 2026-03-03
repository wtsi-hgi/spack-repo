# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynchrony(RPackage):
	"""Methods for Computing Spatial, Temporal, and Spatiotemporal
Statistics

	Methods for computing spatial, temporal, and spatiotemporal
    statistics as described in Gouhier and Guichard (2014) 
    <doi:10.1111/2041-210X.12188>. These methods include 
    empirical univariate, bivariate and multivariate
    variograms; fitting variogram models; phase locking and synchrony analysis;
    generating autocorrelated and cross-correlated matrices.
	"""
	
	homepage = "http://github.com/tgouhier/synchrony"
	cran = "synchrony" 

	version("0.3.8", md5="0224d88b4311c5bba697155c1a07e96b")

