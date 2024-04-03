# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTreeminer(RPackage):
	"""Tree-Based Scan Statistics

	Implementation of unconditional Bernoulli Scan Statistic developed
             by Kulldorff et al. (2003) <doi:10.1111/1541-0420.00039> 
             for hierarchical tree structures. Tree-based Scan Statistics are an
             exploratory method to identify event clusters across the space of a 
             hierarchical tree.
	"""
	
	homepage = "https://entjos.github.io/TreeMineR/"
	cran = "TreeMineR" 

	version("1.0.1", md5="7864f0786aedb706c3e72288a6aed667")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
