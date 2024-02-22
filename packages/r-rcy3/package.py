# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcy3(RPackage):
	"""Functions to Access and Control Cytoscape

	Vizualize, analyze and explore networks using Cytoscape via R. Anything you can do using the graphical user interface of Cytoscape, you can now do with a single RCy3 function.
	"""
	
	homepage = "https://github.com/cytoscape/RCy3"
	bioc = "RCy3" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/RCy3_2.22.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/RCy3/RCy3_2.22.1.tar.gz"]

	version("2.22.1", md5="d4f51eaf382ede111f69aefd2660e383", url="https://www.bioconductor.org/packages/release/bioc/src/contrib/RCy3_2.22.1.tar.gz")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-base64url", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-irkernel", type=("build", "run"))
	depends_on("r-irdisplay", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
