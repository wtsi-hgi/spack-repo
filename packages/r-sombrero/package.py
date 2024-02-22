# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSombrero(RPackage):
	"""SOM Bound to Realize Euclidean and Relational Outputs

	The stochastic (also called on-line) version of the Self-Organising
             Map (SOM) algorithm is provided. Different versions of the
             algorithm are implemented, for numeric and relational data and for
             contingency tables as described, respectively, in Kohonen (2001)
             <isbn:3-540-67921-9>, Olteanu & Villa-Vialaneix (2005)
             <doi:10.1016/j.neucom.2013.11.047> and Cottrell et al (2004)
             <doi:10.1016/j.neunet.2004.07.010>. The package also contains many
             plotting features (to help the user interpret the results), can 
             handle (and impute) missing values and is delivered with a 
             graphical user interface based on 'shiny'.
	"""
	
	homepage = "http://sombrero.clementine.wf/"
	cran = "SOMbrero" 

	version("1.4-2", md5="6a0aa986285411d307bdc23bdc07ea56")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggwordcloud", type=("build", "run"))
	depends_on("r-metr", type=("build", "run"))
	depends_on("r-interp", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
