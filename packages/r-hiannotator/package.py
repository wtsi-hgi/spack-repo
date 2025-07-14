# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHiannotator(RPackage):
	"""Functions for annotating GRanges objects

	hiAnnotator contains set of functions which allow users to annotate a GRanges object with custom set of annotations. The basic philosophy of this package is to take two GRanges objects (query & subject) with common set of seqnames (i.e. chromosomes) and return associated annotation per seqnames and rows from the query matching seqnames and rows from the subject (i.e. genes or cpg islands). The package comes with three types of annotation functions which calculates if a position from query is: within a feature, near a feature, or count features in defined window sizes. Moreover, each function is equipped with parallel backend to utilize the foreach package. In addition, the package is equipped with wrapper functions, which finds appropriate columns needed to make a GRanges object from a common data frame.
	"""
	
	bioc = "hiAnnotator"

	version("1.42.0", commit="cbc1e104e20957e4e31b4b48b05aa20b55692348")
	version("1.36.0", commit="5c4211d26d324403618d782fb614115ce03ccde4")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
