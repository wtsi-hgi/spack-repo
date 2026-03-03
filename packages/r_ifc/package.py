# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIfc(RPackage):
	"""Tools for Imaging Flow Cytometry

	Contains several tools to treat imaging flow cytometry data from 'ImageStream®' and 'FlowSight®' cytometers ('Amnis®' 'Cytek®'). Provides an easy and simple way to read and write .fcs, .rif, .cif and .daf files. Information such as masks, features, regions and populations set within these files can be retrieved for each single cell. In addition, raw data such as images stored can also be accessed. Users, may hopefully increase their productivity thanks to dedicated functions to extract, visualize, manipulate and export 'IFC' data. Toy data example can be installed through the 'IFCdata' package of approximately 32 MB, which is available in a 'drat' repository <https://gitdemont.github.io/IFCdata/>. See file 'COPYRIGHTS' and file 'AUTHORS' for a list of copyright holders and authors.
	"""
	
	cran = "IFC" 

	version("0.2.1", md5="5b89dfc5cbc472fdcaa55c80d21db228")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gridgraphics", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-kernsmooth", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
