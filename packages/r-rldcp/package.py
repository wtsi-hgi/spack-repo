# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRldcp(RPackage):
	"""Text Generation from Data

	Linguistic Descriptions of Complex Phenomena (LDCP) is an architecture and methodology that allows us to model complex phenomena, interpreting input data, and generating automatic text reports customized to the user needs (see <doi:10.1016/j.ins.2016.11.002> and <doi:10.1007/s00500-016-2430-5>). The proposed package contains a set of methods that facilitates the development of LDCP systems. It main goal is increasing the visibility and practical use of this research line.
	"""
	
	homepage = "http://phedes.com/rLDCP"
	cran = "rLDCP" 

	version("1.0.2", md5="aa6d6bfc8b0d2ae2c4b7c43903b0e2c7")

	depends_on("r-xml@3.98.1.4:", type=("build", "run"))
