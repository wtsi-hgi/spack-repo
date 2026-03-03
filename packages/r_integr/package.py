# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIntegr(RPackage):
	"""An Implementation of Interaction Graphs of Aleks Jakulin

	Generates a 'Graphviz' graph of the most significant 3-way 
    interaction gains (i.e. conditional information gains) based on a provided 
    discrete data frame. Various output formats are supported ('Graphviz', SVG, 
    PNG, PDF, PS). For references, see the webpage of Aleks Jakulin 
    <http://stat.columbia.edu/~jakulin/Int/>.
	"""
	
	homepage = "https://github.com/peleplay/integr"
	cran = "integr" 

	version("1.0.0", md5="3c281a368230e8af043d66446ad526b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@0.7.6:", type=("build", "run"))
	depends_on("r-diagrammer@1:", type=("build", "run"))
	depends_on("r-diagrammersvg@0.1:", type=("build", "run"))
	depends_on("r-rsvg@1.3:", type=("build", "run"))
	depends_on("r-gtools@3.5:", type=("build", "run"))
