# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcx(RPackage):
	"""R package implementing the Cytoscape Exchange (CX) format

	Create, handle, validate, visualize and convert networks in the Cytoscape exchange (CX) format to standard data types and objects. The package also provides conversion to and from objects of iGraph and graphNEL. The CX format is also used by the NDEx platform, a online commons for biological networks, and the network visualization software Cytocape.
	"""
	
	homepage = "https://github.com/frankkramer-lab/RCX"
	bioc = "RCX"

	version("1.12.0", commit="546c3dfd1b95377a4aa47c333234c6498ca3634e")
	version("1.6.0", commit="9be752830dca5fec6da69452d3ea1e28ccd9be63")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
