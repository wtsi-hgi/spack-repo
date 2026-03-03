# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNat(RPackage):
	"""NeuroAnatomy Toolbox for Analysis of 3D Image Data

	NeuroAnatomy Toolbox (nat) enables analysis and visualisation of 3D
    biological image data, especially traced neurons. Reads and writes 3D images
    in NRRD and 'Amira' AmiraMesh formats and reads surfaces in 'Amira' hxsurf
    format. Traced neurons can be imported from and written to SWC and 'Amira'
    LineSet and SkeletonGraph formats. These data can then be visualised in 3D
    via 'rgl', manipulated including applying calculated registrations, e.g.
    using the 'CMTK' registration suite, and analysed. There is also a simple
    representation for neurons that have been subjected to 3D skeletonisation
    but not formally traced; this allows morphological comparison between
    neurons including searches and clustering (via the 'nat.nblast' extension
    package).
	"""
	
	homepage = "https://github.com/natverse/nat"
	cran = "nat" 

	version("1.8.24", md5="6031ed2d24ba0b019e724320a948327d")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-rgl@0.98.1:", type=("build", "run"))
	depends_on("r-nabor", type=("build", "run"))
	depends_on("r-igraph@1.3:", type=("build", "run"))
	depends_on("r-filehash@2.3:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-nat-utils@0.4.2:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
