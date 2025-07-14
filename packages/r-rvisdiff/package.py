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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Rvisdiff_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Rvisdiff/Rvisdiff_1.0.0.tar.gz"]

	version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="76a2afecab601bcbfbc0764f6ffaea20593a3cffadc2151d4846482caffd24ea")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
