# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLspls(RPackage):
	"""LS-PLS Models

	Implements the LS-PLS (least squares - partial least squares)
  method described in for instance Jørgensen, K., Segtnan, V. H., Thyholt, K.,
  Næs, T. (2004)  "A Comparison of Methods for Analysing Regression Models with
  Both Spectral and Designed Variables"
  Journal of Chemometrics, 18(10), 451--464, <doi:10.1002/cem.890>.
	"""
	
	homepage = "http://mevik.net/work/software/lspls.html"
	cran = "lspls" 

	version("0.2-2", md5="dad0300fd70228c35397f36033dfc426")

	depends_on("r-pls@2.2:", type=("build", "run"))
