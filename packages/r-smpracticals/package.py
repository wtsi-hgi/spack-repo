# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmpracticals(RPackage):
	"""Practicals for Use with Davison (2003) Statistical Models

	Contains the datasets and a few functions for use with 
        the practicals outlined in Appendix A of the book
        Statistical Models (Davison, 2003, Cambridge University Press), 
        which can be found at <doi:10.1017/CBO9780511815850>.
	"""
	
	homepage = "doi:10.1017/CBO9780511815850"
	cran = "SMPracticals" 

	version("1.4-3.1", md5="7178769cafafe6f993949b8044d9d5a0")

	depends_on("r@1.14:", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
