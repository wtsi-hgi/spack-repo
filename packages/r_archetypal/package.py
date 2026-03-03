# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArchetypal(RPackage):
	"""Finds the Archetypal Analysis of a Data Frame

	Performs archetypal analysis by using Principal Convex Hull Analysis 
    under a full control of all algorithmic parameters. 
    It contains a set of functions for determining the initial solution, the optimal 
    algorithmic parameters and the optimal number of archetypes.
    Post run tools are also available for the assessment of the derived solution. 
    Morup, M., Hansen, LK (2012) <doi:10.1016/j.neucom.2011.06.033>.
    Hochbaum, DS, Shmoys, DB (1985) <doi:10.1287/moor.10.2.180>.
    Eddy, WF (1977) <doi:10.1145/355759.355768>.
    Barber, CB, Dobkin, DP, Huhdanpaa, HT (1996) <doi:10.1145/235815.235821>.    
    Christopoulos, DT (2016) <doi:10.2139/ssrn.3043076>.    
    Falk, A., Becker, A., Dohmen, T., Enke, B., Huffman, D., Sunde, U. (2018), <doi:10.1093/qje/qjy013>. 
    Christopoulos, DT (2015) <doi:10.1016/j.jastp.2015.03.009> .  
    Murari, A., Peluso, E., Cianfrani, Gaudio, F., Lungaroni, M., (2019), <doi:10.3390/e21040394>.    
	"""
	
	cran = "archetypal" 

	version("1.3.0", md5="f1fd4cca9cfea65beeaf4fafe395b54e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-inflection", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-lpsolve", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
