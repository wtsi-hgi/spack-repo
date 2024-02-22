# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPearsonica(RPackage):
	"""Independent Component Analysis using Score Functions from the
Pearson System

	The Pearson-ICA algorithm is a mutual information-based
        method for blind separation of statistically independent source
        signals. It has been shown that the minimization of mutual
        information leads to iterative use of score functions, i.e.
        derivatives of log densities. The Pearson system allows
        adaptive modeling of score functions. The flexibility of the
        Pearson system makes it possible to model a wide range of
        source distributions including asymmetric distributions. The
        algorithm is designed especially for problems with asymmetric
        sources but it works for symmetric sources as well.
	"""
	
	cran = "PearsonICA" 

	version("1.2-5", md5="12ff994eef4ba7b37170f5de4d9734e1")

