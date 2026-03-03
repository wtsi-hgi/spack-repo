# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTree3d(RPackage):
	"""3D Tree Models

	Provides customizable 3D tree models (as 'OBJ' files) for use in data visualization. Includes both planar and solid tree models, various crown types (columnar, oval, palm, pyramidal, rounded, spreading, vase, weeping), and options to change the diameter, height, and color of the tree's crown and trunk.  
	"""
	
	homepage = "https://tylermorganwall.github.io/tree3d/"
	cran = "tree3d" 

	version("0.1.2", md5="42f221bf53404a4867c4fd625bef49c3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rayvertex@0.7.8:", type=("build", "run"))
