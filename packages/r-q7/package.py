# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQ7(RPackage):
	"""Types and Features for Object Oriented Programming

	
    Construct message-passing style objects with types and features. Q7 types uses composition instead of inheritance in creating derived types, allowing defining any code segment as feature and associating any feature to any object. Compared to R6, Q7 is simpler and more flexible, and is more friendly in syntax.  
	"""
	
	cran = "Q7" 

	version("0.1.0", md5="475be3bd69fb9ef194d57c8902230842", url="https://cran.r-project.org/src/contrib/Q7_0.1.0.tar.gz")

	depends_on("r-magrittr", type=("build", "run"))
