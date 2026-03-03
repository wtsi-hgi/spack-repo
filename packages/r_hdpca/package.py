# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdpca(RPackage):
	"""Principal Component Analysis in High-Dimensional Data

	In high-dimensional settings:
	Estimate the number of distant spikes based on the Generalized Spiked Population (GSP) model.
	Estimate the population eigenvalues, angles between the sample and population eigenvectors, correlations between the sample and population PC scores, and the asymptotic shrinkage factors.
	Adjust the shrinkage bias in the predicted PC scores.
	Dey, R. and Lee, S. (2019) <doi:10.1016/j.jmva.2019.02.007>.
	"""
	
	cran = "hdpca" 

	version("1.1.5", md5="843fdb853426a95751bd29c8599aeade")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
