# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNonlineardotplot(RPackage):
	"""Non Linear Dot Plots

	Non linear dot plots are diagrams that allow dots of varying size to be constructed, so that columns with a large number of samples are reduced in height. Implementation of algorithm described in: Nils Rodrigues and Daniel Weiskopf, "Nonlinear Dot Plots", IEEE Transactions on Visualization and Computer Graphics, vol. 24, no. 1, pp. 616-625, 2018. <doi:10.1109/TVCG.2017.2744018>.
	"""
	
	cran = "nonLinearDotPlot" 

	version("0.5.0", md5="18e8b1a0ae1aed15f12e5c1f9fa07bf6")

