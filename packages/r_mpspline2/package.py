# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMpspline2(RPackage):
	"""Mass-Preserving Spline Functions for Soil Data

	A low-dependency implementation of GSIF::mpspline() <https://r-forge.r-project.org/scm/viewvc.php/pkg/R/mpspline.R?view=markup&revision=240&root=gsif>,
  which applies a mass-preserving spline to soil attributes. Splining soil data 
  is a safe way to make continuous down-profile estimates of attributes measured
  over discrete, often discontinuous depth intervals.
	"""
	
	cran = "mpspline2" 

	version("0.1.6", md5="05e5030238c9201ff4cc5b0826281f7d", url="https://cran.r-project.org/src/contrib/mpspline2_0.1.6.tar.gz")

