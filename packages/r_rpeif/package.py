# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpeif(RPackage):
	"""Computation and Plots of Influence Functions for Risk and
Performance Measures

	Computes the influence functions time series of the returns for the risk and 
             performance measures as mentioned in Chen and Martin (2018) 
             <https://www.ssrn.com/abstract=3085672>, as well as in Zhang et al. (2019)
             <https://www.ssrn.com/abstract=3415903>. Also evaluates estimators influence
             functions at a set of parameter values and plots them to display the shapes of 
             the influence functions.
	"""
	
	cran = "RPEIF" 

	version("1.2.4", md5="4630c1f827e7c34a65f7166c2380297d")

	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-robstattm", type=("build", "run"))
