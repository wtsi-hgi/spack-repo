# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIyer517(RPackage):
	"""exprSets for Iyer, Eisen et all 1999 Science paper

	representation of public Iyer data from http://genome-www.stanford.edu/serum/clusters.html
	"""
	
	bioc = "Iyer517" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Iyer517_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Iyer517/Iyer517_1.44.0.tar.gz"]

	version("1.50.0", tag="RELEASE_3_21")
	version("1.44.0", sha256="674e4a4542082c20143e43b29e30eb99664d467b8ecefef61af56a39456750fd", url="https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Iyer517_1.44.0.tar.gz")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

