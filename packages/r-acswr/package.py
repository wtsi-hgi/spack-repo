# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAcswr(RPackage):
	"""A Companion Package for the Book "A Course in Statistics with R"

	A book designed to meet the requirements of masters students. Tattar, P.N., Suresh, R., and Manjunath, B.G. "A Course in Statistics with R", J. Wiley, ISBN 978-1-119-15272-9. 
	"""
	
	cran = "ACSWR" 

	version("1.0", md5="3dfec0ff570e2922849354ac7f578dc4")

	depends_on("r-mass", type=("build", "run"))
