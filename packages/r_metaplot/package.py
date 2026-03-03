# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaplot(RPackage):
	"""Data-Driven Plot Design

	Designs plots in terms of core structure.  See 'example(metaplot)'.
 Primary arguments are (unquoted) column names; order and type (numeric or not)
 dictate the resulting plot.  Specify any y variables, x variable, any groups variable,
 and any conditioning variables to metaplot() to generate density plots, boxplots, 
 mosaic plots, scatterplots, scatterplot matrices, or conditioned plots. Use multiplot() 
 to arrange plots in grids. Wherever present, scalar column attributes 'label' and 'guide' 
 are honored, producing fully annotated plots with minimal effort. Attribute 'guide' 
 is typically units, but may be encoded() to provide interpretations of categorical 
 values (see '?encode').  Utility unpack() transforms scalar column attributes to row 
 values and pack() does the reverse, supporting tool-neutral storage of metadata along 
 with primary data. The package supports customizable aesthetics such as such as reference 
 lines, unity lines, smooths, log transformation, and linear fits. The user may choose
 between trellis and ggplot output. Compact syntax and integrated metadata promote workflow 
 scalability.
	"""
	
	cran = "metaplot" 

	version("0.8.4", md5="6450a7ef5ea239ba13ec1a5be1f094a2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-encode@0.3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr@0.7.1:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
