# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCriticalpath(RPackage):
	"""An Implementation of the Critical Path Method

	
    An R implementation of the Critical Path Method (CPM).
    CPM is a method used to estimate the minimum project duration and determine 
    the amount of scheduling flexibility on the logical network paths within the 
    schedule model. The flexibility is in terms of early start, early finish, 
    late start, late finish, total float and free float. Beside, it permits 
    to quantify the complexity of network diagram through the analysis of 
    topological indicators. Finally, it permits to change the activities duration 
    to perform what-if scenario analysis. The package was built based on following 
    references: To make topological sorting and other graph operation, we use 
    Csardi, G. & Nepusz, T. (2005) 
    <https://www.researchgate.net/publication/221995787_The_Igraph_Software_Package_for_Complex_Network_Research>;
    For schedule concept, the reference was Project Management Institute (2017) 
    <https://www.pmi.org/pmbok-guide-standards/foundational/pmbok>;
    For standards terms, we use Project Management Institute (2017) 
    <https://www.pmi.org/pmbok-guide-standards/lexicon>;
    For algorithms on Critical Path Method development, we use 
    Vanhoucke, M. (2013) <doi:10.1007/978-3-642-40438-2> and 
    Vanhoucke, M. (2014) <doi:10.1007/978-3-319-04331-9>; 
    And, finally, for topological definitions, we use
    Vanhoucke, M. (2009) <doi:10.1007/978-1-4419-1014-1>.
	"""
	
	homepage = "https://rubensjoserosa.com/criticalpath"
	cran = "criticalpath" 

	version("0.2.1", md5="a41c9a6c0987f8aa171cd6de2f23179f")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
