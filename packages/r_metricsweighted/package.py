# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetricsweighted(RPackage):
	"""Weighted Metrics and Performance Measures for Machine Learning

	Provides weighted versions of several metrics and performance
    measures used in machine learning, including average unit deviances of
    the Bernoulli, Tweedie, Poisson, and Gamma distributions, see
    Jorgensen B. (1997, ISBN: 978-0412997112).  The package also contains
    a weighted version of generalized R-squared, see e.g. Cohen, J. et al.
    (2002, ISBN: 978-0805822236).  Furthermore, 'dplyr' chains are
    supported.
	"""
	
	homepage = "https://github.com/mayer79/MetricsWeighted"
	cran = "MetricsWeighted" 

	version("1.0.3", md5="58a21f97edc5d89503d6f52be3c3c438")

	depends_on("r@3.1:", type=("build", "run"))
