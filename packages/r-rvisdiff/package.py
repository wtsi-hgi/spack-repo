# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRvisdiff(RPackage):
	"""Interactive Graphs for Differential Expression

	Creates a muti-graph web page which allows the interactive exploration of differential expression results. The graphical web interface presents results as a table which is integrated with five interactive graphs: MA-plot, volcano plot, box plot, lines plot and cluster heatmap. Graphical aspect and information represented in the graphs can be customized by means of user controls. Final graphics can be exported as PNG format.
	"""
	
	homepage = "https://github.com/BioinfoUSAL/Rvisdiff/"
	bioc = "Rvisdiff" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Rvisdiff_1.0.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Rvisdiff/Rvisdiff_1.0.0.tar.gz"]

	version("1.0.0", md5="3e3b8ccc9cb71388e2e7c17d60995cbe")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
