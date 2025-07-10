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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/hiAnnotator_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/hiAnnotator/hiAnnotator_1.36.0.tar.gz"]

	version("1.36.0", sha256="3e61e8cc67f8ae21fbd9713b1c64a39ecbe74d81f7b9fcb335824efe9783561c")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
