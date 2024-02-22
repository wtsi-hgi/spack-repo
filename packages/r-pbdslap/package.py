# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbdslap(RPackage):
	"""Programming with Big Data -- Scalable Linear Algebra Packages

	Utilizing scalable linear algebra packages mainly
        including 'BLACS', 'PBLAS', and 'ScaLAPACK' in double precision via
        'pbdMPI' based on 'ScaLAPACK' version 2.0.2.
	"""
	
	homepage = "https://pbdr.org/"
	cran = "pbdSLAP" 

	version("0.3-5", md5="b3f319f368796dcbddb1c5b7e73af486")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-pbdmpi@0.3.1:", type=("build", "run"))
	depends_on("openmpi", type=("build", "link", "run"))
