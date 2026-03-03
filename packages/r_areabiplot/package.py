# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAreabiplot(RPackage):
	"""Area Biplot

	Considering an (n x m) data matrix X, this package is based on the method proposed 
             by Gower, Groener, and Velden (2010) <doi:10.1198/jcgs.2010.07134>, and 
             utilize the  resulting matrices from the extended version of the NIPALS decomposition 
             to determine n triangles whose areas are used  to  visually  estimate the elements of
             a specific column of X. After a 90-degree rotation of the sample points, the triangles
             are drawn regarding the following points: 1.the origin of the axes; 2.the sample points;
             3. the vector endpoint representing some variable.
	"""
	
	cran = "areabiplot" 

	version("1.0.0", md5="71ca62ec5661caf530cbdfe60ade29ad")

	depends_on("r-nipals", type=("build", "run"))
