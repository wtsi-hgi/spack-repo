# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RRvenn(RPackage):
    """Set Operations for Many Sets
    
    Set operations for many sets. The base functions for set operations in R can be used for only two sets. This package uses 'purr' to find the union, intersection and difference of three or more sets. This package also provides functions for pairwise set operations among several sets. Further, based on 'ggplot2' and 'ggforce', a Venn diagram can be drawn for two or three sets. For bigger data sets, a clustered heatmap showing presence/absence of the elements of the sets can be drawn based on the 'pheatmap' package. Finally, enrichment test can be applied to two sets whether an overlap is statistically significant or not.
    """

    cran = "RVenn"

    version("1.1.0", sha256="c41a96dd4a9b51e7dcc8647cdbaa0faa704ab22d5b0c1d45e593a6b23b00d504")

    depends_on("r-ggforce", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-magrittr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-vegan", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
