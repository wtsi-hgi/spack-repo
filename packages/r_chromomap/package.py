# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChromomap(RPackage):
	"""Interactive Genomic Visualization of Biological Data

	Provides interactive, configurable and elegant graphics visualization of the chromosomes or chromosome regions
    of any living organism allowing users to map chromosome elements (like genes, SNPs etc.) on the chromosome plot. It introduces
    a special plot viz. the "chromosome heatmap" that, in addition to mapping elements, can visualize the data
    associated with chromosome elements (like gene expression) in the form of heat colors which can be highly
    advantageous in the scientific interpretations and research work. Because of the large size of the chromosomes,
    it is impractical to visualize each element on the same plot. However, the plot provides a magnified view for each
    of chromosome locus to render additional information and visualization specific for that location. You can map
    thousands of genes and can view all mappings easily. Users can investigate the detailed information about the mappings
    (like gene names or total genes mapped on a location) or can view the magnified single or double stranded view of the
    chromosome at a location showing each mapped element in sequential order. The package provide multiple features
    like visualizing multiple sets, chromosome heat-maps, group annotations, adding hyperlinks, and labelling.
    The plots can be saved as HTML documents that can be customized and shared easily. In addition, you can include them in R Markdown or in R 'Shiny' applications.
	"""
	
	cran = "chromoMap" 

	version("4.1.1", md5="4ecdbf84cc94d82e3303b887842b9e10")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-htmltools@0.3.6:", type=("build", "run"))
	depends_on("r-htmlwidgets@1:", type=("build", "run"))
