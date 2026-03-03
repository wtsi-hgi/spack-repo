# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobin(RPackage):
	"""ROBustness in Network

	Assesses the robustness of the community structure of a network found by one or more community detection algorithm to give indications about their reliability. It detects if the community structure found by a set of algorithms is statistically significant and compares the different selected detection algorithms on the same network. robin helps to choose among different community detection algorithms the one that better fits the network of interest. Reference in Policastro V., Righelli D., Carissimo A., Cutillo L., De Feis I. (2021) <https://journal.r-project.org/archive/2021/RJ-2021-040/index.html>.
	"""
	
	homepage = "https://github.com/ValeriaPolicastro/robin"
	cran = "robin" 

	version("1.1.2", md5="61cf65ff4f2198c7e1d448dddf8e6171")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-networkd3", type=("build", "run"))
	depends_on("r-desctools", type=("build", "run"))
	depends_on("r-fdatest", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-spam", type=("build", "run"))
	depends_on("r-qpdf", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
