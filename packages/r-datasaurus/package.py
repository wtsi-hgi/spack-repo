# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatasaurus(RPackage):
	"""Datasets from the Datasaurus Dozen

	The Datasaurus Dozen is a set of datasets with the same
    summary statistics. They retain the same summary statistics despite
    having radically different distributions.  The datasets represent a
    larger and quirkier object lesson that is typically taught via
    Anscombe's Quartet (available in the 'datasets' package). Anscombe's
    Quartet contains four very different distributions with the same
    summary statistics and as such highlights the value of visualisation
    in understanding data, over and above summary statistics. As well as
    being an engaging variant on the Quartet, the data is generated in a
    novel way. The simulated annealing process used to derive datasets
    from the original Datasaurus is detailed in "Same Stats, Different
    Graphs: Generating Datasets with Varied Appearance and Identical
    Statistics through Simulated Annealing" <doi:10.1145/3025453.3025912>.
	"""
	
	homepage = "https://github.com/jumpingrivers/datasauRus"
	cran = "datasauRus" 

	version("0.1.8", md5="6023af4f909e4f309c9faa723a85929d")
	version("0.1.6", md5="99991fa1c109073e008fff5e920e292d")

	depends_on("r@3.5:", type=("build", "run"))
