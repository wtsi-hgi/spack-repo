# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnect(RPackage):
	"""Contingency Measure-Based Networks for Binary Time Series

	The ConNEcT approach investigates the pairwise association strength of binary time series by calculating contingency measures and depicts the results in a network. The package includes features to explore and visualize the data. To calculate the pairwise concurrent or temporal sequenced relationship between the variables, the package provides seven contingency measures (proportion of agreement, classical & corrected Jaccard, Cohen's kappa, phi correlation coefficient, odds ratio, and log odds ratio), however, others can easily be implemented. The package also includes non-parametric significance tests, that can be applied to test whether the contingency value quantifying the relationship between the variables is significantly higher than chance level. Most importantly this test accounts for auto-dependence and relative frequency.See Bodner et al.(2021) <doi: 10.1111/bmsp.12222>.Finally, a network can be drawn. Variables depicted the nodes of the network, with the node size adapted to the prevalence. The association strength between the variables defines the undirected (concurrent) or directed (temporal sequenced) links between the nodes. The results of the non-parametric significance test can be included by depicting either all links or only the significant ones. Tutorial see Bodner et al.(2021) <doi:10.3758/s13428-021-01760-w>.
	"""
	
	cran = "ConNEcT" 

	version("0.7.27", md5="c0055295d361ad3bab0fe1ed71cc5899")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-qgraph", type=("build", "run"))
