# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgw(RPackage):
	"""Bunch-Gay-Welsch Statistical Estimation

	Performs statistical estimation and inference-related computations
   by accessing and executing modified versions of 'Fortran' subroutines 
   originally published in the Association for Computing Machinery (ACM) 
   journal Transactions on Mathematical Software (TOMS) by Bunch, Gay and 
   Welsch (1993) <doi:10.1145/151271.151279>. The acronym 'BGW' (from the 
   authors' last names) will be used when making reference to technical 
   content (e.g., algorithm, methodology) that originally appeared in ACM TOMS.
   A key feature of BGW is that it exploits the special structure of statistical 
   estimation problems within a trust-region-based optimization approach to 
   produce an estimation algorithm that is much more effective than the usual 
   practice of using optimization methods and codes originally developed for 
   general optimization. The 'bgw' package bundles 'R' wrapper (and related) 
   functions with modified 'Fortran' source code so that it can be compiled and 
   linked in the 'R' environment for fast execution. This version implements 
   a function ('bgw_mle.R') that performs maximum likelihood estimation (MLE) 
   for a user-provided model object that computes probabilities (a.k.a. 
   probability densities). The motivation for producing this initial version 
   is to provide fast, efficient, and reliable MLE for discrete choice models 
   that can be called from the 'Apollo' choice modelling 'R' package: 
   see <http://www.apollochoicemodelling.com>. However, estimation can also be 
   performed in a stand-alone fashion without using 'Apollo' (as shown in simple 
   examples). After this initial version is available on CRAN, an updated 
   version of 'Apollo' (0.2.9) will be made available that automatically loads 
   'bgw'. Additional development can then occur, including more detailed 
   examples in 'bgw' that refer to 'Apollo.' Note also that BGW capabilities 
   are not limited to MLE, and future extension to other estimators (e.g., 
   nonlinear least squares, generalized method of moments, etc.) is possible. 
   The 'Fortran' code included in 'bgw' was modified by one of the 
   original BGW authors (Bunch) under his rights as confirmed by direct 
   consultation with the ACM Intellectual Property and Rights Manager.  See 
   <https://authors.acm.org/author-resources/author-rights>. The main 
   requirement is clear citation of the original publication (see above). 
	"""
	
	cran = "bgw" 

	version("0.1.3", md5="2aefeee43a088c799b616118d1aba4a8")
	version("0.1.2", md5="846e9c0b57871e9dad3729c1e40b840a")

	depends_on("r@4:", type=("build", "run"))
