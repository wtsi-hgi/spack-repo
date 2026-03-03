# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFddm(RPackage):
	"""Fast Implementation of the Diffusion Decision Model

	Provides the probability density function (PDF), cumulative
  distribution function (CDF), and the partial derivatives of the PDF of the
  diffusion decision model (DDM; e.g.,
  Ratcliff & McKoon, 2008, <doi:10.1162/neco.2008.12-06-420>) with across-trial
  variability in the drift rate. Because the PDF, its partial derivatives, and
  the CDF of the DDM both contain an infinite sum, they need to be approximated.
  'fddm' implements all published approximations
  (Navarro & Fuss, 2009, <doi:10.1016/j.jmp.2009.02.003>;
  Gondan, Blurton, & Kesselmeier, 2014, <doi:10.1016/j.jmp.2014.05.002>;
  Blurton, Kesselmeier, & Gondan, 2017, <doi:10.1016/j.jmp.2016.11.003>;
  Hartmann & Klauer, 2021, <doi:10.1016/j.jmp.2021.102550>) plus
  new approximations. All approximations are implemented purely in 'C++'
  providing faster speed than existing packages.
	"""
	
	homepage = "https://github.com/rtdists/fddm"
	cran = "fddm" 

	version("0.5-2", md5="3a78c8ec37e65c56828622a74f22f1c1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
