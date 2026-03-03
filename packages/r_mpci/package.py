# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpci(RPackage):
	"""Multivariate Process Capability Indices (MPCI)

	It performs the followings Multivariate Process Capability Indices: Shahriari et al. (1995) Multivariate Capability Vector, Taam et al. (1993) Multivariate Capability Index (MCpm), Pan and Lee (2010) proposal (NMCpm) and the followings based on Principal Component Analysis (PCA):Wang and Chen (1998), Xekalaki and Perakis (2002) and Wang (2005). Two datasets are included. 
	"""
	
	cran = "MPCI" 

	version("1.0.7", md5="d0ffc2f1769e6accc9453435ca59fd1a")

	depends_on("r@3.1:", type=("build", "run"))
